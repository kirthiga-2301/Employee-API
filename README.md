# Employee Management API (FastAPI)

This is a FastAPI-based practice assignment for managing employee records using MongoDB.

## Features
- **POST /employees**: Create a new employee with Name, Role, and City.
- **GET /employees/{id}**: Fetch employee details using their ID.
- **Persistent Storage**: Uses MongoDB for data storage.
- **Input Validation**: Uses Pydantic to ensure all fields are provided.

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Database Configuration**:
   - Ensure MongoDB is running on your machine.
   - Update the `MONGO_URL` in the `.env` file if necessary.

3. **Run the Application**:
   ```bash
   python -m uvicorn main:app --reload
   ```

4. **Testing**:
   - Access the interactive API docs at: `http://127.0.0.1:8000/docs`
   - Import the `postman_collection.json` into Postman for manual testing.

## GitHub Instructions
1. Initialize git: `git init`
2. Add files: `git add .`
3. Commit: `git commit -m "Complete Employee API assignment"`
4. Push to your repository.
