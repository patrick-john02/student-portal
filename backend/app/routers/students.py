from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db import Student, get_async_session
from app.schemas import StudentCreate, StudentRead
from app.users import current_active_user

router = APIRouter(
    prefix="/students",
    tags=["Students"],
    dependencies=[Depends(current_active_user)],
)


# ---------- CREATE STUDENT ----------
@router.post("/", response_model=StudentRead, status_code=status.HTTP_201_CREATED)
async def create_student(
    student: StudentCreate,
    db: AsyncSession = Depends(get_async_session),
):
    new_student = Student(**student.model_dump())
    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)
    return new_student


# ---------- READ ALL STUDENTS ----------
@router.get("/", response_model=list[StudentRead])
async def get_students(db: AsyncSession = Depends(get_async_session)):
    result = await db.execute(select(Student))
    students = result.scalars().all()
    return students


# ---------- READ SINGLE STUDENT ----------
@router.get("/{student_id}", response_model=StudentRead)
async def get_student(student_id: int, db: AsyncSession = Depends(get_async_session)):
    result = await db.execute(select(Student).where(Student.id == student_id))
    student = result.scalar_one_or_none()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


# ---------- UPDATE STUDENT ----------
@router.put("/{student_id}", response_model=StudentRead)
async def update_student(
    student_id: int,
    updated_data: StudentCreate,
    db: AsyncSession = Depends(get_async_session),
):
    result = await db.execute(select(Student).where(Student.id == student_id))
    existing = result.scalar_one_or_none()
    if not existing:
        raise HTTPException(status_code=404, detail="Student not found")

    for key, value in updated_data.model_dump().items():
        setattr(existing, key, value)

    db.add(existing)
    await db.commit()
    await db.refresh(existing)
    return existing


# ---------- DELETE STUDENT ----------
@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(student_id: int, db: AsyncSession = Depends(get_async_session)):
    result = await db.execute(select(Student).where(Student.id == student_id))
    student = result.scalar_one_or_none()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    await db.delete(student)
    await db.commit()
    return None
