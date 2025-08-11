# 🚀 FastAPI Blog API with JWT Authentication (Updated 2025)

This is a REST API for managing blog posts with JWT authentication.  
Based on a tutorial from 2021, fully updated to work with the latest libraries and best practices.

---

## 📌 Features

- User registration
- JWT authentication login
- Full CRUD for blogs (JWT protected)
- One-to-many relationship between Users and Blogs
- Organized project structure using **routers** and **repositories**

---

## 🛠 Technologies

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- SQLite
- JWT (PyJWT)
- Passlib (bcrypt)

---

## 📂 Project structure

blog/
├── repository/
│ ├── blog.py # Blog CRUD logic
│ └── user.py # User CRUD logic
├── routers/
│ ├── auth.py # Login & token generation
│ ├── blog.py # Blog routes
│ └── user.py # User routes
├── database.py # Database connection & session
├── hashing.py # Password hashing utilities
├── models.py # SQLModel database models
├── oauth2.py # JWT token authentication
├── schemas.py # Pydantic schemas
└── token.py # JWT creation & verification
main.py # Application entry point
requirements.txt # Dependencies


---

## ⚙️ How to run

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/fastapi-blog-auth.git
   cd fastapi-blog-auth

2. **Create and activate a virtual environment**
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. **Install dependencies**
pip install -r requirements.txt

4. **Run the server**
uvicorn main:app --reload

5. **Access interactive API docs**
Swagger UI: http://127.0.0.1:8000/docs#
ReDoc: http://127.0.0.1:8000/redoc

## 🔑 Main Endpoints

| Method | Route        | Description                 | Access     |
|--------|--------------|-----------------------------|------------|
| POST   | `/auth`      | Login (generate JWT token)  | Public     |
| POST   | `/user`      | Create user                  | Public     |
| GET    | `/blog`      | List all blogs               | Protected  |
| POST   | `/blog`      | Create new blog              | Protected  |
| GET    | `/blog/{id}` | Get a blog by ID             | Protected  |
| PUT    | `/blog/{id}` | Update a blog                | Protected  |
| DELETE | `/blog/{id}` | Delete a blog                | Protected  |

---

## 📝 Credits
Based on the [FastAPI Course by Bitfumes](https://github.com/bitfumes/fastapi-course) (2021).  
Updated for FastAPI 2025 by **Raysa Rocha**.