from enum import StrEnum


class Status(StrEnum):
    RACKED = "racked"
    OS_INSTALLED = "os-installed"
    REACHABLE = "reachable"
    VERIFIED = "verified"
    PLANNED = "planned"
    IN_USE = "in-use"
    UNIDENTIFIED = "unidentified"
