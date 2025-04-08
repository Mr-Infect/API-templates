# 🛠️ CRUD API Template (Python)

A production-ready FastAPI-based CRUD API template.

## ⚙️ Features
- Create, Read, Update, Delete
- Pagination
- Partial Updates
- Soft Delete (is_active)

## 📦 API Endpoints
- `GET /items/`
- `GET /items/{id}`
- `POST /items/`
- `PATCH /items/{id}`
- `DELETE /items/{id}`

## 🧪 Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Access Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
