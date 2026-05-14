# Employee Management API

A simple REST API built using FastAPI and MongoDB Atlas to manage employee records. This project is a Python Capstone project designed to demonstrate clean coding standards, proper exception handling, and database integration.

## Features
- **Add new employees**: Automatically generates unique numerical IDs.
- **Get employee by ID**: Returns specific details including a derived "Salary Category".
- **Filter employees**: Search by department using case-insensitive query parameters.
- **Delete employee**: Remove records by their unique ID.
- **Data Validation**: Ensures non-empty fields and positive salary values.

## Tech Used
- **FastAPI**: Modern web framework for building APIs.
- **MongoDB Atlas**: Cloud-hosted NoSQL database.
- **Pydantic**: Data validation and settings management.
- **Uvicorn**: ASGI server for running the application.

## Project Structure
```text
Employee-API/
├── main.py
├── models.py
├── database.py
├── routes.py
├── .env
├── .python-version
├── uv.lock
├── requirements.txt
└── README.md
```

## Setup
### 1. Clone the project
```bash
git clone https://github.com/kirthiga-2301/Employee-API.git
cd Employee-API
```

### 2. Create virtual environment
```bash
python -m venv venv
```
Activate it:
- **Windows**: `venv\Scripts\activate`
- **Mac/Linux**: `source venv/bin/activate`

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add environment variables
Create a `.env` file in the root directory:
```text
MONGO_URL=your_mongodb_atlas_connection_string
```

## Run the Server
```bash
uvicorn main:app --reload
```
Server runs at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Endpoints
### Create Employee
**POST** `/employees`

Example request:
```json
{
  "name": "Kavi",
  "role": "Developer",
  "department": "Engineering",
  "city": "Los Angeles",
  "salary": 85000,
  "active": true,
  "skills": ["Python", "FastAPI"]
}
```

### Get Employee by ID
**GET** `/employees/{employee_id}`

Returns name, department, active status, salary, and salary category.
- **High salary**: salary >= 50000
- **Normal salary**: salary < 50000

### Filter by Department
**GET** `/employees?department={name}`

### Delete Employee
**DELETE** `/employees/{employee_id}`

## API Documentation
FastAPI provides built-in interactive docs:
- **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Notes
- Employee names must be unique.
- Duplicate records with identical details are blocked.
- Proper HTTP status codes (201, 200, 400, 404) are used throughout the API.
