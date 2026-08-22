from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from ..enums import Kind, Status


@dataclass(frozen=True, slots=True)
class Node:
    name: str
    kind: Kind
    role: str
    status: Status
    address: str | None = None
    mac: str | None = None
    hardware: str | None = None
    os: str | None = None
    interface: str | None = None
    switch_port: str | None = None
    hypervisor: str | None = None
    location: str | None = None
    rack: str | None = None

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "Node":
        return cls(
            **{**data, "kind": Kind(data["kind"]), "status": Status(data["status"])}
        )
