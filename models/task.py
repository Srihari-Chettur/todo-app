from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    subject_id: int
    done: bool
    description: str
    subject_id: int