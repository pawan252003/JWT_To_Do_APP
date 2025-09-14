# To-Do App with JWT Authentication

A secure and efficient To-Do application built with **Flask** and **Flask-JWT-Extended** for user authentication. Data is persistently stored in **SQLite**, ensuring lightweight and fast database operations. The application is fully **deployed on Render** for easy access and scalability. Endpoints are thoroughly tested using **Postman**, providing a robust and reliable API experience.

---
## 🌐 Live Demo
Check out the live app here: https://jwt-to-do-app.onrender.com

## 🚀 Features

- User registration & login with JWT authentication  
- Secure CRUD operations for tasks (create, read, update, delete)  
- SQLite database integration  
- Structured project with routes & models  
- Ready for deployment (**Render compatible**)  

---

## ⚙️ Tech Stack

- **Backend:** Flask, Flask-JWT-Extended  
- **Database:** SQLite  
- **Deployment:** Render(Procfile included)  
- **Testing:** Postman  

---

## 📌 API Endpoints

### 🔑 Authentication
- `POST /register` → Register a new user  
- `POST /login` → Login and get JWT token  

### ✅ Tasks
- `GET /tasks` → Get all tasks (JWT required)  
- `POST /tasks` → Create a new task (JWT required)  
- `PUT /tasks/<id>` → Update a task (JWT required)  
- `DELETE /tasks/<id>` → Delete a task (JWT required)  

---

## ▶️ Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/pawan252003/jwt-todo-app.git
cd jwt-todo-app

```

### 2️⃣ Create virtual environment & install dependencies
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Run the app
```
python run.py
```

App will start at: http://127.0.0.1:5000/

---

### Testing with Postman

- Register or Login to get a JWT token.
- Use the token in Authorization → Bearer Token for accessing /tasks endpoints.
- Perform CRUD operations on tasks.

---
### 📦 Deployment

- This repo includes:
- requirements.txt
- Procfile

