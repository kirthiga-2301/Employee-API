# Employee API Assignment

This is my practice project for the FastAPI assignment. I've built a simple API to manage employee records using MongoDB.

### How to get it running:
- First, install the requirements using: `pip install -r requirements.txt`
- Make sure your MongoDB is running (I used the local one at `mongodb://localhost:27017/`).
- To start the server, just run: `python -m uvicorn main:app --reload`

### What it does:
- `POST /employees`: You can create a new employee. Just send the name, role, and city in the body.
- `GET /employees`: This will show you a list of all the employees you've added.
- `GET /employees/{id}`: You can fetch a specific employee using their ID.

I also added a `postman_collection.json` file in the folder so you can test the endpoints easily.
