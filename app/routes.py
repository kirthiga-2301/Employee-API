from fastapi import APIRouter, HTTPException, Query
from app.models import Employee
from app.database import employees_collection

router = APIRouter()

@router.post("/employees", status_code=201)
def create_employee(employee: Employee):
    if not employee.name or not employee.role or not employee.department or not employee.city:
        raise HTTPException(status_code=400, detail="Text fields (name, role, department, city) cannot be empty")
    
    if employee.salary <= 0:
        raise HTTPException(status_code=400, detail="Salary must be a positive number")
        
    duplicate_employee = employees_collection.find_one({
        "name": employee.name,
        "role": employee.role,
        "department": employee.department,
        "city": employee.city,
        "salary": employee.salary,
        "active": employee.active
    })
    if duplicate_employee:
        raise HTTPException(status_code=400, detail="Identical employee record already exists")

    existing_employee = employees_collection.find_one({"name": employee.name})
    if existing_employee:
        raise HTTPException(status_code=400, detail="Employee with this name already exists")
        
    emp_dict = employee.dict()
    
    last_employee = employees_collection.find_one(sort=[("id", -1)])
    if last_employee:
        next_id = last_employee["id"] + 1
    else:
        next_id = 1
    emp_dict["id"] = next_id
    
    employees_collection.insert_one(emp_dict.copy())
    
    return emp_dict

@router.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    emp = employees_collection.find_one({"id": employee_id})
    if emp:
        if emp["salary"] >= 50000:
            salary_category = "High salary"
        else:
            salary_category = "Normal salary"
        
        return {
            "name": emp["name"],
            "department": emp["department"],
            "active status": emp["active"],
            "salary": emp["salary"],
            "salary category": salary_category
        }
    
    raise HTTPException(status_code=404, detail="Employee not found")

@router.get("/employees")
def filter_employees(department: str = Query(None, description="Filter employees by department")):
    query = {}
    if department:
        query["department"] = {"$regex": f"^{department}$", "$options": "i"}
    
    cursor = employees_collection.find(query, {"_id": 0})
    return list(cursor)

@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    result = employees_collection.delete_one({"id": employee_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return {"message": f"Employee with ID {employee_id} has been successfully deleted"}
