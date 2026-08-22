from pathlib import Path
from typing import Final


class Paths:
    ROOT: Final[Path] = Path(__file__).resolve().parent.parent
    ROSTER: Final[Path] = ROOT / "inventory" / "nodes.yml"
    BUILD: Final[Path] = ROOT / "build"
