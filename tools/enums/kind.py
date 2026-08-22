from enum import StrEnum


class Kind(StrEnum):
    PHYSICAL = "physical"
    VIRTUAL = "virtual"
    APPLIANCE = "appliance"
    FOREIGN = "foreign"
