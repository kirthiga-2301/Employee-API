# Employee Management API (Capstone Project)

This is a FastAPI-based Employee Management API built as a Capstone project. It allows for creating, fetching, and filtering employee records stored in MongoDB.

## Features
- **Proper Project Structure**: Organized into `app/` modules.
- **Pydantic Models**: Data validation and serialization.
- **MongoDB Integration**: Persistent storage.
- **Endpoints**:
  - `POST /employees`: Create a new employee.
  - `GET /employees/{id}`: Fetch specific employee details with derived salary category.
  - `GET /employees`: Filter employees by department via query parameters.
- **Exception Handling**: Proper `HTTPException` usage for error scenarios (400, 404).

## Project Structure
```text
Employee/
    app/
        __init__.py
        main.py
        models.py
        database.py
        routes.py
    requirements.txt
    README.md
    .gitignore
    postman_collection.json
```

## How to Run
1. **Setup Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure MongoDB**:
   Ensure MongoDB is running locally or provide a `MONGO_URL` in the `.env` file.
4. **Start the Application**:
   ```bash
   uvicorn app.main:app --reload
   ```

## Testing
- **Swagger UI**: Access `http://127.0.0.1:8000/docs` to test via the interactive UI.
- **Postman**: Import the `postman_collection.json` file into Postman.
