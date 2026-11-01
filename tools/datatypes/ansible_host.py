from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any

from .node import Node


@dataclass(frozen=True, slots=True)
class AnsibleHost:
    ansible_host: str
    place_role: str
    place_interface: str | None
    ansible_become_exe: str | None = None

    @classmethod
    def of(cls, node: Node) -> "AnsibleHost":
        return cls(
            ansible_host=node.address,
            place_role=node.role,
            place_interface=node.interface,
            # ansible.cfg assumes the sudo that ships beside sudo-rs on 26.04
            ansible_become_exe=None if (node.os or "").startswith("Ubuntu 26") else "/usr/bin/sudo",
        )

    def as_dict(self) -> dict[str, Any]:
        return {
            key: str(value) if isinstance(value, Enum) else value
            for key, value in asdict(self).items()
            if value is not None
        }
