# db.py
# Database setup for Senior High School Student Portal
# (FastAPI + SQLAlchemy + Async SQLite + FastAPI-Users)

from typing import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Date,
    Float,
    Text,
    Enum,
    Boolean,
    UniqueConstraint,
)
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
import enum
import uuid
import os


# ---------- DATABASE CONFIG ----------
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./student_portal.db")

engine = create_async_engine(DATABASE_URL, echo=False, future=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


# ---------- FASTAPI-USERS USER MODEL ----------
class User(SQLAlchemyBaseUserTableUUID, Base):
    full_name = Column(String(150), nullable=False)
    role = Column(String(20), default="Student")  # Admin, Teacher, Student


# ---------- ENUMS ----------
class StrandEnum(str, enum.Enum):
    STEM = "STEM"
    ABM = "ABM"
    HUMSS = "HUMSS"
    TVL = "TVL"
    GAS = "GAS"


class SemesterEnum(str, enum.Enum):
    FIRST = "1st Semester"
    SECOND = "2nd Semester"


class RoleEnum(str, enum.Enum):
    ADMIN = "Admin"
    TEACHER = "Teacher"
    STUDENT = "Student"


# ---------- MODELS ----------
class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Enum(RoleEnum), unique=True, nullable=False)
    description = Column(Text, nullable=True)


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String(20), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    contact_no = Column(String(20))
    specialization = Column(String(100))

    advisory_section = relationship("Section", back_populates="adviser", uselist=False)
    subjects = relationship("Subject", back_populates="teacher")


class Section(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    strand = Column(Enum(StrandEnum), nullable=False)
    adviser_id = Column(Integer, ForeignKey("teachers.id", ondelete="SET NULL"), nullable=True)

    adviser = relationship("Teacher", back_populates="advisory_section")
    students = relationship("Student", back_populates="section")


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String(20), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    middle_name = Column(String(100))
    last_name = Column(String(100), nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(String(10))
    address = Column(Text)
    strand = Column(Enum(StrandEnum), nullable=False)
    section_id = Column(Integer, ForeignKey("sections.id", ondelete="SET NULL"))
    guardian_name = Column(String(150))
    guardian_contact = Column(String(20))
    active = Column(Boolean, default=True)

    section = relationship("Section", back_populates="students")
    grades = relationship("Grade", back_populates="student")


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(150), nullable=False)
    semester = Column(Enum(SemesterEnum), nullable=False)
    strand = Column(Enum(StrandEnum), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id", ondelete="SET NULL"))

    teacher = relationship("Teacher", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject")


class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"))
    quarter = Column(Integer, nullable=False)
    score = Column(Float, nullable=False)

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")

    __table_args__ = (
        UniqueConstraint("student_id", "subject_id", "quarter", name="uq_grade_per_quarter"),
    )


# ---------- DEPENDENCIES ----------
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


async def get_user_db(
    session: AsyncSession = Depends(get_async_session),
) -> AsyncGenerator[SQLAlchemyUserDatabase, None]:
    yield SQLAlchemyUserDatabase(session, User)


# ---------- INIT FUNCTION ----------
async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ SQLite database initialized successfully.")


if __name__ == "__main__":
    import asyncio

    asyncio.run(init_db())
