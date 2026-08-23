from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any

from .node import Node


@dataclass(frozen=True, slots=True)
class AnsibleHost:
    ansible_host: str
    place_role: str
    place_interface: str | None

    @classmethod
    def of(cls, node: Node) -> "AnsibleHost":
        return cls(
            ansible_host=node.address,
            place_role=node.role,
            place_interface=node.interface,
        )

    def as_dict(self) -> dict[str, Any]:
        return {
            key: str(value) if isinstance(value, Enum) else value
            for key, value in asdict(self).items()
        }
