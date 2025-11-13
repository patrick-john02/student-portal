# app.py
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.db import init_db, get_async_session, User, Student
from app.users import fastapi_users, auth_backend, current_active_user
from app.schemas import UserRead, UserCreate, StudentRead, StudentCreate

from app.routers.students import router as student_router


# ============================================================
# LIFESPAN (replaces deprecated @app.on_event("startup"))
# ============================================================
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Initializing database...")
    await init_db()
    yield
    print("🛑 Shutting down...")


# ============================================================
# MAIN APP
# ============================================================
app = FastAPI(
    title="Senior High School Student Portal",
    lifespan=lifespan
)


# ============================================================
# AUTH ROUTES
# ============================================================
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"]
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"]
)

app.include_router(
    fastapi_users.get_users_router(UserRead),
    prefix="/users",
    tags=["Users"]
)


# ============================================================
# STUDENT ROUTER
# ============================================================
app.include_router(student_router)


# ============================================================
# ROOT
# ============================================================
@app.get("/")
async def root():
    return {"message": "Student Portal API is running 🚀"}
