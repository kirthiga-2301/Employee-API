from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")

try:
    client = MongoClient(MONGO_URL)
    db = client["employee_db"]
    collection = db["employees"]
    
    client.server_info()
    
    if "localhost" in MONGO_URL or "127.0.0.1" in MONGO_URL:
        print("✅ Local MongoDB is connected and working!")
    else:
        print("✅ MongoDB Atlas (Cloud) is connected and working!")
        
except Exception as e:
    print(f" Connection error: {e}")

def save_employee(name: str, role: str, city: str):
    employee_data = {
        "name": name,
        "role": role,
        "city": city
    }
    collection.insert_one(employee_data)
    return collection.count_documents({})

def get_employee_by_id(emp_id: int):
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
    cursor = collection.find().skip(emp_id - 1).limit(1)
    doc = next(cursor, None)
    
    if doc:
        collection.delete_one({"_id": doc["_id"]})
        return True
    return False