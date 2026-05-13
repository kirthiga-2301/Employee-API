from pydantic import BaseModel, Field

class EmployeeBase(BaseModel):
    name: str = Field(..., min_length=1, description="Name of the employee")
    role: str = Field("Employee", description="Current role of the employee")
    city: str = Field("Not Specified", description="City where the employee is based")

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    employee_id: int
