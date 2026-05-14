from fastapi import FastAPI, HTTPException
from models import Employee, EmployeeCreate
import db

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Employee Management API is running! Use /employees for the API."}

@app.post("/employees", status_code=201)
def create_employee(employee: EmployeeCreate):
    emp_id = db.save_employee(
        employee.name, 
        employee.role, 
        employee.city
    )
    
    return {
        "message": "Employee created successfully",
        "employee": {
            "employee_id": emp_id,
            **employee.model_dump()
        }
    }

@app.get("/employees")
def get_all_employees():
    return db.get_all_employees()

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    employee = db.get_employee_by_id(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: EmployeeCreate):
    success = db.update_employee(
        employee_id,
        employee.name,
        employee.role,
        employee.city
    )
    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return {
        "message": "Employee updated successfully",
        "employee": {
            "employee_id": employee_id,
            **employee.model_dump()
        }
    }

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    success = db.delete_employee(employee_id)
    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return {"message": "Employee deleted successfully"}
