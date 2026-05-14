from pydantic import BaseModel
from typing import List

class Employee(BaseModel):
    name: str
    role: str
    department: str
    city: str
    salary: float
    active: bool
    skills: List[str] = []
