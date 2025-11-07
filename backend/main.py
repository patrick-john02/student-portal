# main.py
from fastapi import FastAPI
from app.routers import students, teachers, subjects
from app.users import fastapi_users, auth_backend
from app.db import User
from app.schemas import UserRead, UserCreate

app = FastAPI(title="Senior High School Portal")

# ---------- AUTH ROUTES ----------
app.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"])
app.include_router(fastapi_users.get_register_router(UserRead, UserCreate), prefix="/auth", tags=["auth"])

# ---------- CUSTOM ROUTES ----------
app.include_router(students.router)
app.include_router(teachers.router)
app.include_router(subjects.router)

@app.get("/")
async def root():
    return {"message": "API running 🚀"}

# ✅ Optional: this is ONLY for direct python execution
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
