from dataclasses import asdict, dataclass
from typing import Any

from .node import Node


@dataclass(frozen=True, slots=True)
class VmSpec:
    name: str
    os: str
    address: str
    mac: str
    interface: str
    memory: str
    vcpus: int
    disk: str

    @classmethod
    def of(cls, node: Node) -> "VmSpec":
        fields = (node.os, node.address, node.mac, node.interface, node.memory, node.vcpus, node.disk)
        if None in fields:
            raise ValueError(f"{node.name}: a virtual machine needs os, address, mac, interface, memory, vcpus and disk")
        return cls(node.name, *fields)

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)
