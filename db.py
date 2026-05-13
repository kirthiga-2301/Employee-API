from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")

# Connect to MongoDB
client = MongoClient(MONGO_URL)
db = client["employee_db"]
collection = db["employees"]

def save_employee(name: str, role: str, city: str):
    # MongoDB stores data as documents
    employee_data = {
        "name": name,
        "role": role,
        "city": city
    }
    result = collection.insert_one(employee_data)
    # We use the document count as a simple ID for your assignment practice
    return collection.count_documents({})

def get_employee_by_id(emp_id: int):
    # Since MongoDB uses ObjectIds, but your assignment uses numeric IDs, 
    # we simulate the ID lookup by skipping to the Nth document
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