from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Network:
    cidr: str
    gateway: str
