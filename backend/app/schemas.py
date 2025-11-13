# schemas.py
from datetime import date, datetime, time
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from enum import Enum

from app.db import StrandEnum, SemesterEnum   # <-- IMPORTANT FIX
import uuid
from fastapi_users import schemas as fastapi_users_schemas


# =========================
# ENUMS
# =========================
class GradeLevelEnum(str, Enum):
    GRADE_11 = "Grade 11"
    GRADE_12 = "Grade 12"


class AttendanceStatusEnum(str, Enum):
    PRESENT = "Present"
    ABSENT = "Absent"
    LATE = "Late"
    EXCUSED = "Excused"


# =========================
# STUDENT
# =========================
class StudentBase(BaseModel):
    student_id: str
    lrn: Optional[str] = None
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    birth_date: date
    gender: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    zip_code: Optional[str] = None
    email: Optional[EmailStr] = None
    contact_no: Optional[str] = None
    strand: StrandEnum
    grade_level: GradeLevelEnum
    guardian_name: Optional[str] = None
    guardian_contact: Optional[str] = None
    guardian_email: Optional[EmailStr] = None
    emergency_contact: Optional[str] = None
    blood_type: Optional[str] = None
    medical_conditions: Optional[str] = None
    active: Optional[bool] = True


class StudentCreate(StudentBase):
    pass


class StudentRead(StudentBase):
    id: int

    class Config:
        from_attributes  = True


# =========================
# SECTION
# =========================
class SectionBase(BaseModel):
    name: str
    strand: StrandEnum
    grade_level: GradeLevelEnum
    room_number: Optional[str] = None
    capacity: Optional[int] = 40


# =========================
# SUBJECT
# =========================
class SubjectBase(BaseModel):
    code: str
    name: str
    description: Optional[str] = None
    semester: SemesterEnum
    strand: StrandEnum
    grade_level: GradeLevelEnum
    units: Optional[int] = 1
    hours_per_week: Optional[int] = None


# =========================
# GRADES
# =========================
class GradeBase(BaseModel):
    quarter: int = Field(..., ge=1, le=4)
    written_work: Optional[float] = None
    performance_task: Optional[float] = None
    quarterly_exam: Optional[float] = None
    final_grade: float = Field(..., ge=0, le=100)
    remarks: Optional[str] = None


class GradeCreate(GradeBase):
    student_id: int
    subject_id: int


# =========================
# ATTENDANCE
# =========================
class AttendanceCreate(BaseModel):
    student_id: int
    subject_id: Optional[int] = None
    date: date
    status: AttendanceStatusEnum
    time_in: Optional[time] = None
    time_out: Optional[time] = None
    remarks: Optional[str] = None


class AttendanceRead(AttendanceCreate):
    id: int

    class Config:
        from_attributes  = True


# =========================
# ASSIGNMENT
# =========================
class AssignmentCreate(BaseModel):
    subject_id: int
    title: str
    description: Optional[str] = None
    assignment_type: Optional[str] = None
    total_points: float
    due_date: datetime


class AssignmentRead(AssignmentCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes  = True


# =========================
# ENROLLMENT
# =========================
class EnrollmentCreate(BaseModel):
    student_id: int
    section_id: Optional[int] = None
    school_year_id: int
    grade_level: GradeLevelEnum
    date_enrolled: date


class EnrollmentRead(EnrollmentCreate):
    id: int
    enrollment_status: str

    class Config:
        from_attributes  = True


# =========================
# SCHOOL YEAR
# =========================
class SchoolYearCreate(BaseModel):
    year_start: int
    year_end: int
    is_active: bool = False
    start_date: Optional[date] = None
    end_date: Optional[date] = None


class SchoolYearRead(SchoolYearCreate):
    id: int

    class Config:
        from_attributes  = True


# =========================
# ANNOUNCEMENTS
# =========================
class AnnouncementCreate(BaseModel):
    title: str
    content: str
    priority: str = "Normal"
    target_audience: Optional[str] = None
    section_id: Optional[int] = None
    expires_at: Optional[datetime] = None


class AnnouncementRead(AnnouncementCreate):
    id: int
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes  = True

class TeacherBase(BaseModel):
    employee_id: str
    first_name: str
    last_name: str
    email: EmailStr
    contact_no: Optional[str] = None
    specialization: Optional[str] = None
    department: Optional[str] = None
    active: Optional[bool] = True

class TeacherCreate(TeacherBase):
    pass

class TeacherRead(TeacherBase):
    id: int
    class Config:
        from_attributes  = True


class SubjectCreate(SubjectBase):
    teacher_id: Optional[int] = None

class SubjectRead(SubjectBase):
    id: int
    teacher_id: Optional[int] = None
    class Config:
        from_attributes  = True


# =========================
# SECTION
# =========================
class SectionCreate(SectionBase):
    adviser_id: Optional[int] = None
    school_year_id: Optional[int] = None

class SectionRead(SectionBase):
    id: int
    adviser_id: Optional[int] = None
    school_year_id: Optional[int] = None
    class Config:
        from_attributes  = True


# =========================
# GRADE
# =========================
class GradeRead(GradeBase):
    id: int
    student_id: int
    subject_id: int
    date_encoded: datetime
    class Config:
        from_attributes  = True


# =========================
# USER
# =========================
class UserRead(fastapi_users_schemas.BaseUser[uuid.UUID]):
    full_name: str
    role: str

class UserCreate(fastapi_users_schemas.BaseUserCreate):
    full_name: str
    role: str = "Student"

class UserUpdate(fastapi_users_schemas.BaseUserUpdate):
    full_name: Optional[str] = None
    role: Optional[str] = None