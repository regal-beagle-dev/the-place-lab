import sys
from pathlib import Path

import yaml

from ..datatypes import AnsibleHost, Roster
from ..paths import Paths


class _NoAliases(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


class NodeRenderer:
    TARGETS = ("ssh_config", "hosts", "hosts.yml")
    COMMANDS = ("render", "check", "reservations")

    def __init__(self, roster: Roster | None = None, build: Path | None = None) -> None:
        self.roster = roster or Roster.load()
        self.build_dir = build or Paths.BUILD

    def build(self, target: str) -> str:
        return getattr(self, f"build_{target.replace('.', '_')}")()

    def build_ssh_config(self) -> str:
        return "".join(
            f"Host {node.name}\n"
            f"    HostName {node.address}\n"
            f"    User {self.roster.admin_user}\n\n"
            for node in self.roster.reachable
        )

    def build_hosts(self) -> str:
        width = max(len(n.address) for n in self.roster.addressed)
        return "".join(
            f"{node.address:<{width}}  {node.name}\n" for node in self.roster.addressed
        )

    def build_hosts_yml(self) -> str:
        groups: dict[str, dict] = {}
        for node in self.roster.managed:
            group = str(node.role).replace("-", "_")
            groups.setdefault(group, {}).setdefault("hosts", {})[node.name] = (
                AnsibleHost.of(node).as_dict()
            )
        inventory = {
            "all": {
                "vars": {"ansible_user": self.roster.admin_user},
                "children": groups,
            }
        }
        return yaml.dump(inventory, Dumper=_NoAliases, sort_keys=False)

    def is_current(self, target: str) -> bool:
        path = self.build_dir / target
        return path.exists() and path.read_text() == self.build(target)

    def render(self) -> None:
        self.build_dir.mkdir(exist_ok=True)
        for target in self.TARGETS:
            (self.build_dir / target).write_text(self.build(target))

    def check(self) -> None:
        stale = [t for t in self.TARGETS if not self.is_current(t)]
        if stale:
            sys.exit(f"stale, run `place render`: {', '.join(stale)}")

    def reservations(self) -> None:
        for node in self.roster.reservable:
            print(f"{node.name:<8} {node.address:<16} {node.mac or '?'}")

    def run(self, argv: list[str] | None = None) -> None:
        args = sys.argv[1:] if argv is None else argv
        command = args[0] if args else "render"
        if command not in self.COMMANDS:
            sys.exit(f"usage: place [{'|'.join(self.COMMANDS)}]")
        getattr(self, command)()
