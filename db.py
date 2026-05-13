from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load connection link from .env file
load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")

try:
    # Set up the connection
    client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)
    db = client["employee_db"]
    collection = db["employees"]
    
    # Check if connection is successful
    client.server_info()
    print("✅ Connected to MongoDB successfully!")
except Exception as e:
    print(f"❌ Error connecting to MongoDB: {e}")

def save_employee(name: str, role: str, city: str):
    """Saves a new employee and returns the total count as their ID"""
    employee_data = {
        "name": name,
        "role": role,
        "city": city
    }
    collection.insert_one(employee_data)
    return collection.count_documents({})

def get_employee_by_id(emp_id: int):
    """Finds an employee by skipping to their position in the list"""
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