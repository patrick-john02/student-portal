# db.py
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
    DateTime,
    Float,
    Text,
    Enum,
    Boolean,
    UniqueConstraint,
    Time,
)
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
import enum
import os
from datetime import datetime


# ---------- DATABASE CONFIG ----------
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./student_portal.db")

engine = create_async_engine(DATABASE_URL, echo=False, future=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


# ---------- FASTAPI-USERS USER MODEL ----------
class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"
    full_name = Column(String(150), nullable=False)
    role = Column(String(20), default="Student")  # Admin / Teacher / Student
    profile_picture = Column(String(500))
    phone_number = Column(String(20))
    last_login = Column(DateTime)


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
    PARENT = "Parent"


class GradeLevelEnum(str, enum.Enum):
    GRADE_11 = "Grade 11"
    GRADE_12 = "Grade 12"


class AttendanceStatusEnum(str, enum.Enum):
    PRESENT = "Present"
    ABSENT = "Absent"
    LATE = "Late"
    EXCUSED = "Excused"


class AssignmentStatusEnum(str, enum.Enum):
    PENDING = "Pending"
    SUBMITTED = "Submitted"
    GRADED = "Graded"
    LATE = "Late"


class EventTypeEnum(str, enum.Enum):
    ACADEMIC = "Academic"
    EXTRACURRICULAR = "Extracurricular"
    HOLIDAY = "Holiday"
    EXAM = "Exam"
    MEETING = "Meeting"


class PaymentStatusEnum(str, enum.Enum):
    PAID = "Paid"
    PENDING = "Pending"
    OVERDUE = "Overdue"
    PARTIAL = "Partial"


# ---------- CORE TABLES ----------
class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Enum(RoleEnum), unique=True, nullable=False)
    description = Column(Text)
    permissions = Column(Text)  # JSON string of permissions


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String(20), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    contact_no = Column(String(20))
    specialization = Column(String(100))
    department = Column(String(100))
    hire_date = Column(Date)
    active = Column(Boolean, default=True)

    advisory_section = relationship("Section", back_populates="adviser", uselist=False)
    subjects = relationship("Subject", back_populates="teacher")
    consultations = relationship("Consultation", back_populates="teacher")


class Section(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    strand = Column(Enum(StrandEnum), nullable=False)
    grade_level = Column(Enum(GradeLevelEnum), nullable=False)
    room_number = Column(String(20))
    capacity = Column(Integer, default=40)
    adviser_id = Column(Integer, ForeignKey("teachers.id", ondelete="SET NULL"))
    school_year_id = Column(Integer, ForeignKey("school_years.id"))

    adviser = relationship("Teacher", back_populates="advisory_section")
    students = relationship("Student", back_populates="section")
    schedules = relationship("Schedule", back_populates="section")
    school_year = relationship("SchoolYear")


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String(20), unique=True, nullable=False)
    lrn = Column(String(20), unique=True)  # Learner Reference Number
    first_name = Column(String(100), nullable=False)
    middle_name = Column(String(100))
    last_name = Column(String(100), nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(String(10))
    address = Column(Text)
    city = Column(String(100))
    province = Column(String(100))
    zip_code = Column(String(10))
    email = Column(String(120))
    contact_no = Column(String(20))
    strand = Column(Enum(StrandEnum), nullable=False)
    grade_level = Column(Enum(GradeLevelEnum), nullable=False)
    section_id = Column(Integer, ForeignKey("sections.id", ondelete="SET NULL"))
    guardian_name = Column(String(150))
    guardian_contact = Column(String(20))
    guardian_email = Column(String(120))
    emergency_contact = Column(String(20))
    blood_type = Column(String(5))
    medical_conditions = Column(Text)
    enrollment_date = Column(Date)
    active = Column(Boolean, default=True)

    section = relationship("Section", back_populates="students")
    grades = relationship("Grade", back_populates="student")
    attendance = relationship("Attendance", back_populates="student")
    assignments = relationship("AssignmentSubmission", back_populates="student")
    payments = relationship("Payment", back_populates="student")
    disciplinary_records = relationship("DisciplinaryRecord", back_populates="student")
    medical_records = relationship("MedicalRecord", back_populates="student")


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(150), nullable=False)
    description = Column(Text)
    semester = Column(Enum(SemesterEnum), nullable=False)
    strand = Column(Enum(StrandEnum), nullable=False)
    grade_level = Column(Enum(GradeLevelEnum), nullable=False)
    units = Column(Integer, default=1)
    hours_per_week = Column(Integer)
    teacher_id = Column(Integer, ForeignKey("teachers.id", ondelete="SET NULL"))
    prerequisites = Column(Text)  # JSON string of prerequisite subject IDs

    teacher = relationship("Teacher", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject")
    schedules = relationship("Schedule", back_populates="subject")
    assignments = relationship("Assignment", back_populates="subject")
    learning_materials = relationship("LearningMaterial", back_populates="subject")


class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"))
    quarter = Column(Integer, nullable=False)
    written_work = Column(Float)
    performance_task = Column(Float)
    quarterly_exam = Column(Float)
    final_grade = Column(Float, nullable=False)
    remarks = Column(String(20))  # Passed, Failed, INC
    date_encoded = Column(DateTime, default=datetime.utcnow)
    encoded_by = Column(Integer, ForeignKey("user.id"))

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")
    encoder = relationship("User")

    __table_args__ = (
        UniqueConstraint("student_id", "subject_id", "quarter", name="uq_grade_per_quarter"),
    )


# ---------- SCHEDULING ----------
class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"))
    section_id = Column(Integer, ForeignKey("sections.id", ondelete="CASCADE"))
    day_of_week = Column(String(10), nullable=False)  # Monday, Tuesday, etc.
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    room = Column(String(20))
    school_year_id = Column(Integer, ForeignKey("school_years.id"))

    subject = relationship("Subject", back_populates="schedules")
    section = relationship("Section", back_populates="schedules")
    school_year = relationship("SchoolYear")


# ---------- SCHOOL YEAR & ENROLLMENT ----------
class SchoolYear(Base):
    __tablename__ = "school_years"

    id = Column(Integer, primary_key=True, index=True)
    year_start = Column(Integer, nullable=False)
    year_end = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=False)
    start_date = Column(Date)
    end_date = Column(Date)

    enrollments = relationship("Enrollment", back_populates="school_year")
    schedules = relationship("Schedule", back_populates="school_year")
    sections = relationship("Section", back_populates="school_year")


class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    section_id = Column(Integer, ForeignKey("sections.id", ondelete="SET NULL"))
    school_year_id = Column(Integer, ForeignKey("school_years.id", ondelete="CASCADE"))
    grade_level = Column(Enum(GradeLevelEnum), nullable=False)
    date_enrolled = Column(Date, nullable=False)
    enrollment_status = Column(String(20), default="Active")  # Active, Dropped, Transferred
    remarks = Column(Text)

    student = relationship("Student")
    section = relationship("Section")
    school_year = relationship("SchoolYear", back_populates="enrollments")

    __table_args__ = (
        UniqueConstraint("student_id", "school_year_id", name="uq_student_enrollment"),
    )


# ---------- ATTENDANCE ----------
class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="SET NULL"))
    date = Column(Date, nullable=False)
    status = Column(Enum(AttendanceStatusEnum), nullable=False)
    time_in = Column(Time)
    time_out = Column(Time)
    remarks = Column(Text)
    recorded_by = Column(Integer, ForeignKey("user.id"))

    student = relationship("Student", back_populates="attendance")
    subject = relationship("Subject")
    recorder = relationship("User")


# ---------- ASSIGNMENTS & ASSESSMENTS ----------
class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"))
    title = Column(String(200), nullable=False)
    description = Column(Text)
    assignment_type = Column(String(50))  # Homework, Project, Quiz, Exam
    total_points = Column(Float, nullable=False)
    due_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    created_by = Column(Integer, ForeignKey("user.id"))
    attachment_url = Column(String(500))

    subject = relationship("Subject", back_populates="assignments")
    creator = relationship("User")
    submissions = relationship("AssignmentSubmission", back_populates="assignment")


class AssignmentSubmission(Base):
    __tablename__ = "assignment_submissions"

    id = Column(Integer, primary_key=True, index=True)
    assignment_id = Column(Integer, ForeignKey("assignments.id", ondelete="CASCADE"))
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    submission_date = Column(DateTime, default=datetime.utcnow)
    status = Column(Enum(AssignmentStatusEnum), default=AssignmentStatusEnum.PENDING)
    content = Column(Text)
    attachment_url = Column(String(500))
    score = Column(Float)
    feedback = Column(Text)
    graded_by = Column(Integer, ForeignKey("user.id"))
    graded_at = Column(DateTime)

    assignment = relationship("Assignment", back_populates="submissions")
    student = relationship("Student", back_populates="assignments")
    grader = relationship("User")

    __table_args__ = (
        UniqueConstraint("assignment_id", "student_id", name="uq_student_submission"),
    )


# ---------- LEARNING MATERIALS ----------
class LearningMaterial(Base):
    __tablename__ = "learning_materials"

    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"))
    title = Column(String(200), nullable=False)
    description = Column(Text)
    material_type = Column(String(50))  # PDF, Video, Link, Document
    file_url = Column(String(500))
    uploaded_by = Column(Integer, ForeignKey("user.id"))
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    is_public = Column(Boolean, default=False)

    subject = relationship("Subject", back_populates="learning_materials")
    uploader = relationship("User")


# ---------- ANNOUNCEMENTS & EVENTS ----------
class Announcement(Base):
    __tablename__ = "announcements"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    content = Column(Text, nullable=False)
    priority = Column(String(20), default="Normal")  # Urgent, High, Normal, Low
    target_audience = Column(String(50))  # All, Students, Teachers, Specific Section
    section_id = Column(Integer, ForeignKey("sections.id", ondelete="SET NULL"))
    created_by = Column(Integer, ForeignKey("user.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime)
    is_active = Column(Boolean, default=True)
    attachment_url = Column(String(500))

    creator = relationship("User")
    section = relationship("Section")


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(Text)
    event_type = Column(Enum(EventTypeEnum), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    location = Column(String(200))
    organizer_id = Column(Integer, ForeignKey("user.id"))
    is_public = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    organizer = relationship("User")


# ---------- PAYMENTS & FEES ----------
class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    school_year_id = Column(Integer, ForeignKey("school_years.id"))
    payment_type = Column(String(50), nullable=False)  # Tuition, Miscellaneous, Books, etc.
    amount = Column(Float, nullable=False)
    amount_paid = Column(Float, default=0.0)
    balance = Column(Float)
    status = Column(Enum(PaymentStatusEnum), default=PaymentStatusEnum.PENDING)
    due_date = Column(Date)
    payment_date = Column(Date)
    payment_method = Column(String(50))  # Cash, Bank Transfer, Online
    reference_number = Column(String(100))
    remarks = Column(Text)
    recorded_by = Column(Integer, ForeignKey("user.id"))

    student = relationship("Student", back_populates="payments")
    school_year = relationship("SchoolYear")
    recorder = relationship("User")


# ---------- DISCIPLINARY & MEDICAL ----------
class DisciplinaryRecord(Base):
    __tablename__ = "disciplinary_records"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    incident_date = Column(Date, nullable=False)
    incident_type = Column(String(100))  # Minor, Major, Behavioral
    description = Column(Text, nullable=False)
    action_taken = Column(Text)
    reported_by = Column(Integer, ForeignKey("user.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    student = relationship("Student", back_populates="disciplinary_records")
    reporter = relationship("User")


class MedicalRecord(Base):
    __tablename__ = "medical_records"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    visit_date = Column(Date, nullable=False)
    chief_complaint = Column(String(200))
    diagnosis = Column(Text)
    treatment = Column(Text)
    prescribed_medication = Column(Text)
    attending_personnel = Column(String(150))
    follow_up_date = Column(Date)
    remarks = Column(Text)

    student = relationship("Student", back_populates="medical_records")


# ---------- CONSULTATION & MESSAGES ----------
class Consultation(Base):
    __tablename__ = "consultations"

    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id", ondelete="CASCADE"))
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    consultation_date = Column(DateTime, nullable=False)
    purpose = Column(String(200))
    notes = Column(Text)
    status = Column(String(20), default="Scheduled")  # Scheduled, Completed, Cancelled
    created_at = Column(DateTime, default=datetime.utcnow)

    teacher = relationship("Teacher", back_populates="consultations")
    student = relationship("Student")


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    recipient_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    subject = Column(String(200))
    content = Column(Text, nullable=False)
    sent_at = Column(DateTime, default=datetime.utcnow)
    is_read = Column(Boolean, default=False)
    read_at = Column(DateTime)
    parent_message_id = Column(Integer, ForeignKey("messages.id"))  # For threading

    sender = relationship("User", foreign_keys=[sender_id])
    recipient = relationship("User", foreign_keys=[recipient_id])


# ---------- ACTIVITY LOGS & FILE UPLOADS ----------
class ActivityLog(Base):
    __tablename__ = "activity_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    action = Column(String(255), nullable=False)
    entity_type = Column(String(50))  # Student, Grade, Attendance, etc.
    entity_id = Column(Integer)
    ip_address = Column(String(45))
    user_agent = Column(String(255))
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")


class FileUpload(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    uploaded_by = Column(Integer, ForeignKey("user.id"))
    related_to = Column(String(50))  # Student, Assignment, Material, etc.
    related_id = Column(Integer)
    filename = Column(String(255), nullable=False)
    filepath = Column(String(500), nullable=False)
    file_size = Column(Integer)  # in bytes
    file_type = Column(String(50))
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    description = Column(Text)

    uploader = relationship("User")


# ---------- ADDITIONAL FEATURES ----------
class AcademicHonor(Base):
    __tablename__ = "academic_honors"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    school_year_id = Column(Integer, ForeignKey("school_years.id"))
    honor_type = Column(String(100))  # With High Honors, With Honors, etc.
    quarter = Column(Integer)
    date_awarded = Column(Date)
    remarks = Column(Text)

    student = relationship("Student")
    school_year = relationship("SchoolYear")


class ClubMembership(Base):
    __tablename__ = "club_memberships"

    id = Column(Integer, primary_key=True, index=True)
    club_name = Column(String(100), nullable=False)
    description = Column(Text)
    adviser_id = Column(Integer, ForeignKey("teachers.id"))
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    position = Column(String(50))  # Member, Officer, President, etc.
    joined_date = Column(Date)
    is_active = Column(Boolean, default=True)

    adviser = relationship("Teacher")
    student = relationship("Student")


# ==========================================================
#                 SESSION / USERS
# ==========================================================

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


async def get_user_db(
    session: AsyncSession = Depends(get_async_session),
):
    yield SQLAlchemyUserDatabase(session, User)


# ==========================================================
#                 INIT DB
# ==========================================================

async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Database initialized successfully with all tables.")


async def reset_db() -> None:
    """Drop all tables and recreate them"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Database reset complete!")

# Update the __main__ section:
if __name__ == "__main__":
    import asyncio
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--reset":
        asyncio.run(reset_db())
    else:
        asyncio.run(init_db())