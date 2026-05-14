from fastapi import APIRouter, HTTPException, Query
from app.models import Employee
from app.database import employees_collection

router = APIRouter()

@router.post("/employees", status_code=201)
def create_employee(employee: Employee):
    """
    POST endpoint to create and store employee data.
    Adds a unique numerical ID automatically.
    """
    # 1. Validation: Ensure no fields are empty
    if not employee.name or not employee.role or not employee.department or not employee.city:
        raise HTTPException(status_code=400, detail="Text fields (name, role, department, city) cannot be empty")
    
    # 2. Validation: Ensure salary is a positive number
    if employee.salary <= 0:
        raise HTTPException(status_code=400, detail="Salary must be a positive number")
        
    # 3. Full Duplicate Check: Check if an employee with the exact same details already exists
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

    # 4. Name Uniqueness Check: Check if name already exists
    existing_employee = employees_collection.find_one({"name": employee.name})
    if existing_employee:
        raise HTTPException(status_code=400, detail="Employee with this name already exists")
        
    emp_dict = employee.dict()
    
    # Add numerical ID automatically (finding the highest ID and incrementing)
    last_employee = employees_collection.find_one(sort=[("id", -1)])
    if last_employee:
        next_id = last_employee["id"] + 1
    else:
        next_id = 1
    emp_dict["id"] = next_id
    
    # Save to MongoDB
    employees_collection.insert_one(emp_dict.copy())
    
    return emp_dict

@router.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    """
    GET endpoint to fetch employee details by employee ID.
    Returns specific fields: name, department, active status, salary, and salary category.
    """
    emp = employees_collection.find_one({"id": employee_id})
    if emp:
        # Derived message: salary category using explicit if-else
        if emp["salary"] >= 50000:
            salary_category = "High salary"
        else:
            salary_category = "Normal salary"
        
        # Return response in dictionary format with specific fields
        return {
            "name": emp["name"],
            "department": emp["department"],
            "active status": emp["active"],
            "salary": emp["salary"],
            "salary category": salary_category
        }
    
    # Proper error message if record is not found
    raise HTTPException(status_code=404, detail="Employee not found")

@router.get("/employees")
def filter_employees(department: str = Query(None, description="Filter employees by department")):
    """
    GET endpoint to filter employees by department using query parameters.
    Returns multiple records as a list of dictionaries.
    """
    query = {}
    if department:
        # Case insensitive match for department
        query["department"] = {"$regex": f"^{department}$", "$options": "i"}
    
    # Fetch from MongoDB, excluding the internal MongoDB _id object
    cursor = employees_collection.find(query, {"_id": 0})
    return list(cursor)

@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    """
    DELETE endpoint to remove an employee by their unique ID.
    """
    result = employees_collection.delete_one({"id": employee_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return {"message": f"Employee with ID {employee_id} has been successfully deleted"}
