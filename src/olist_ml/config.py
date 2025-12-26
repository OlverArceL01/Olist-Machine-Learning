from dataclasses import dataclass

@dataclass
class Project:
    root_path: str
    epoch: int

@dataclass
class OlistConfig:
    project: Project