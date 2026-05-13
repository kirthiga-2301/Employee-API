# 🚀 FastAPI Employee Management API

A professional Employee Management API built with **FastAPI** and **MongoDB Atlas (Cloud)**. This project demonstrates a full-stack backend flow with virtual environment isolation and cloud database integration.

## ✨ Features
*   **Full CRUD Support**: Create, Read, and List employees.
*   **FastAPI Framework**: High performance, easy to use, and auto-generated Swagger UI.
*   **MongoDB Atlas**: Live cloud database for secure and scalable data storage.
*   **Pydantic Models**: Robust data validation and serialization.
*   **Virtual Environment**: Fully isolated project environment using `venv`.

## 🛠️ Technology Stack
*   **Backend**: Python, FastAPI
*   **Database**: MongoDB Atlas (NoSQL)
*   **Environment**: Python Virtual Environment (venv)
*   **Testing**: Postman, Swagger UI

## 📁 Project Structure
*   `main.py`: Core API endpoints and server configuration.
*   `db.py`: Database connection logic and CRUD operations.
*   `models.py`: Pydantic schemas for data validation.
*   `.env`: Secret environment variables (Cloud Connection String).
*   `.vscode/`: Custom VS Code settings for environment sync.

## 🚀 How to Run
1. **Clone the repository**:
   ```bash
   git clone https://github.com/kirthiga-2301/Employee-API.git
   ```
2. **Setup Virtual Environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure Database**:
   Create a `.env` file and add your MongoDB Atlas URL:
   ```env
   MONGO_URL=mongodb+srv://<username>:<password>@cluster0.xxx.mongodb.net/
   ```
5. **Start the Server**:
   ```bash
   python -m uvicorn main:app --reload
   ```

## 🧪 API Documentation
Once the server is running, visit:
👉 `http://127.0.0.1:8000/docs` to see the interactive Swagger UI.

---
Built with ❤️ by Kirthiga
