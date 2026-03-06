from dataclasses import dataclass
from typing import Optional

@dataclass
class Task:
    id: int
    title: str
    subject_id: int
    done: bool
    subject_id: int
    due_date: Optional[str] = None