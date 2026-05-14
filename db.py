from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load connection settings from .env
load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")

try:
    # Connect to MongoDB
    client = MongoClient(MONGO_URL)
    db = client["employee_db"]
    collection = db["employees"]
    
    # Check connection
    client.server_info()
    
    # Check if it's local or cloud
    if "localhost" in MONGO_URL or "127.0.0.1" in MONGO_URL:
        print("✅ Local MongoDB is connected and working!")
    else:
        print("✅ MongoDB Atlas (Cloud) is connected and working!")
        
except Exception as e:
    print(f" Connection error: {e}")

def save_employee(name: str, role: str, city: str):
    """Saves a new employee to the database"""
    employee_data = {
        "name": name,
        "role": role,
        "city": city
    }
    collection.insert_one(employee_data)
    return collection.count_documents({})

def get_employee_by_id(emp_id: int):
    """Fetches an employee from the database by ID"""
    cursor = collection.find().skip(emp_id - 1).limit(1)
    doc = next(cursor, None)
    
    if doc:
        return {
            "employee_id": emp_id,
            "name": doc["name"],
            "role": doc["role"],
            "city": doc["city"]
        }
    return None

def get_all_employees():
    """Returns a list of all employees in the database"""
    employees = []
    cursor = collection.find()
    for i, doc in enumerate(cursor, 1):
        employees.append({
            "employee_id": i,
            "name": doc["name"],
            "role": doc["role"],
            "city": doc["city"]
        })
    return employees

def update_employee(emp_id: int, name: str, role: str, city: str):
    """Updates an existing employee by ID"""
    # First, find the document to get its _id based on our sequence logic
    cursor = collection.find().skip(emp_id - 1).limit(1)
    doc = next(cursor, None)
    
    if doc:
        collection.update_one(
            {"_id": doc["_id"]},
            {"$set": {"name": name, "role": role, "city": city}}
        )
        return True
    return False

def delete_employee(emp_id: int):
    """Deletes an employee from the database by ID"""
    # Find the document to get its _id based on our sequence logic
    cursor = collection.find().skip(emp_id - 1).limit(1)
    doc = next(cursor, None)
    
    if doc:
        collection.delete_one({"_id": doc["_id"]})
        return True
    return False