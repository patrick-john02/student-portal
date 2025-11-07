# schemas.py
# Pydantic Schemas for Senior High School Student Portal

from datetime import date
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
import uuid


# ---------- ENUMS ----------
class StrandEnum(str, Enum):
    STEM = "STEM"
    ABM = "ABM"
    HUMSS = "HUMSS"
    TVL = "TVL"
    GAS = "GAS"


class SemesterEnum(str, Enum):
    FIRST = "1st Semester"
    SECOND = "2nd Semester"


class RoleEnum(str, Enum):
    ADMIN = "Admin"
    TEACHER = "Teacher"
    STUDENT = "Student"


# ---------- USER SCHEMAS ----------
class UserRead(BaseModel):
    id: uuid.UUID
    email: EmailStr
    full_name: str
    role: str
    is_active: bool

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    role: str = "Student"  # Default role for new users


class UserUpdate(BaseModel):
    full_name: Optional[str]
    password: Optional[str]
    role: Optional[str]
    is_active: Optional[bool]


# ---------- TEACHER SCHEMAS ----------
class TeacherBase(BaseModel):
    employee_id: str
    first_name: str
    last_name: str
    email: EmailStr
    contact_no: Optional[str]
    specialization: Optional[str]


class TeacherCreate(TeacherBase):
    pass


class TeacherRead(TeacherBase):
    id: int

    class Config:
        orm_mode = True


# ---------- SECTION SCHEMAS ----------
class SectionBase(BaseModel):
    name: str
    strand: StrandEnum


class SectionCreate(SectionBase):
    adviser_id: Optional[int]


class SectionRead(SectionBase):
    id: int
    adviser_id: Optional[int]

    class Config:
        orm_mode = True


# ---------- STUDENT SCHEMAS ----------
class StudentBase(BaseModel):
    student_id: str
    first_name: str
    middle_name: Optional[str]
    last_name: str
    birth_date: date
    gender: Optional[str]
    address: Optional[str]
    strand: StrandEnum
    guardian_name: Optional[str]
    guardian_contact: Optional[str]
    active: Optional[bool] = True


class StudentCreate(StudentBase):
    section_id: Optional[int]


class StudentRead(StudentBase):
    id: int
    section_id: Optional[int]

    class Config:
        orm_mode = True


# ---------- SUBJECT SCHEMAS ----------
class SubjectBase(BaseModel):
    code: str
    name: str
    semester: SemesterEnum
    strand: StrandEnum


class SubjectCreate(SubjectBase):
    teacher_id: Optional[int]


class SubjectRead(SubjectBase):
    id: int
    teacher_id: Optional[int]

    class Config:
        orm_mode = True


# ---------- GRADE SCHEMAS ----------
class GradeBase(BaseModel):
    quarter: int = Field(..., ge=1, le=4)
    score: float = Field(..., ge=0, le=100)


class GradeCreate(GradeBase):
    student_id: int
    subject_id: int


class GradeRead(GradeBase):
    id: int
    student_id: int
    subject_id: int

    class Config:
        orm_mode = True
