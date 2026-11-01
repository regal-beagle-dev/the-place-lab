from enum import StrEnum


class Role(StrEnum):
    STORAGE = "storage"
    CONTROL_PLANE = "control-plane"
    HYPERVISOR = "hypervisor"
    WORKER = "worker"
    BAY = "bay"
    SWITCH = "switch"
    WORKSTATION = "workstation"
    CONSOLE = "console"
    UNKNOWN = "unknown"
