from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar

import yaml

from ..enums import Kind, Status
from ..paths import Paths
from .lab import Lab
from .node import Node


@dataclass(frozen=True, slots=True)
class Roster:
    PATH: ClassVar[Path] = Paths.ROSTER

    lab: Lab
    nodes: tuple[Node, ...]

    @classmethod
    def load(cls, path: Path | None = None) -> "Roster":
        data = yaml.safe_load((path or cls.PATH).read_text())
        return cls(
            lab=Lab.from_mapping(data["lab"]),
            nodes=tuple(Node.from_mapping(n) for n in data["nodes"]),
        )

    @property
    def admin_user(self) -> str:
        return self.lab.admin_user

    def of_kind(self, *kinds: Kind) -> Sequence[Node]:
        return [n for n in self.nodes if n.kind in kinds]

    @property
    def reachable(self) -> Sequence[Node]:
        return [
            n
            for n in self.of_kind(Kind.PHYSICAL, Kind.VIRTUAL)
            if n.status is not Status.PLANNED
        ]

    @property
    def managed(self) -> Sequence[Node]:
        return [n for n in self.of_kind(Kind.PHYSICAL) if n.status is not Status.PLANNED]

    @property
    def reservable(self) -> Sequence[Node]:
        return self.of_kind(Kind.PHYSICAL, Kind.APPLIANCE)
