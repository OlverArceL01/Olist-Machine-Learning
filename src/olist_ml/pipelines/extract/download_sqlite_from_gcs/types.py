from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class OutputPaths:
    zip_path: Path
    sqlite_path: Path