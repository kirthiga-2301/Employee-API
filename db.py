from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load connection settings from .env
load_dotenv()

# Use Local MongoDB URL
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")

try:
    # Connect to Local MongoDB
    client = MongoClient(MONGO_URL)
    db = client["employee_db"]
    collection = db["employees"]
    
    # Check if connection is successful
    client.server_info()
    print("✅ Local MongoDB is connected and working!")
except Exception as e:
    print(f"❌ Connection error: {e}")

def save_employee(name: str, role: str, city: str):
    """Saves a new employee to the local database"""
    employee_data = {
        "name": name,
        "role": role,
        "city": city
    }
    collection.insert_one(employee_data)
    # Returns the count as a simple ID
    return collection.count_documents({})

def get_employee_by_id(emp_id: int):
    """Fetches an employee from the local database by ID"""
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
    """Returns a list of all employees in the local database"""
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