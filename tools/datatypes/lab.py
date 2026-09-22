from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from .network import Network


@dataclass(frozen=True, slots=True)
class Lab:
    admin_user: str
    domain: str
    network: Network

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> Lab:
        return cls(
            admin_user=data["admin_user"],
            domain=data["domain"],
            network=Network(**data["network"]),
        )
