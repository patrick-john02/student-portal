from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db import Teacher, get_async_session
from app.schemas import TeacherCreate, TeacherRead
from app.users import current_active_user


router = APIRouter(
    prefix = '/teachers',
    tags = ['Teachers'],
    dependencies = [Depends(current_active_user)],
)

@router.post('/', response_model = TeacherRead, status_code = status.HTTP_201_CREATED)
async def create_teacher(
    teacher: TeacherCreate,
    db: AsyncSession = Depends(get_async_session),
):
    new_teacher = Teacher(**teacher.model_dump())
    db.add(new_teacher)
    await db.commit
    await db.refresh(new_teacher)
    return new_teacher


@router.get('/', response_model =list[TeacherRead])
async def get_teacher(db: AsyncSession = Depends(get_async_session )):
    result = await db.execute(select(Teacher))
    teachers = result.scalars().all()
    return teachers


@router.get("/{teacher_id}", response_model = TeacherRead)
async def get_teacher(teacher_id: int, db: AsyncSession = Depends(get_async_session)):
    result = await db.execute(select(Teacher).where(Teacher.id == teacher_id))
    teacher = result.scalar_one_or_none()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not Found")
    return teacher


@router.put("/{teacher_id}", response_model = TeacherRead)
async def update_teacher(teacher_id: int, updated_data: TeacherCreate, db: AsyncSession = Depends(get_async_session)):
    result = await db.execute(select(Teacher).where(Teacher.id == teacher_id))
    existing = result.scalar_one_or_none()
    if not existing:
        raise HTTPException(status_code = 404, detail = "teacher not found")
    
    for key , value in updated_data.model_dump().items():
        setattr(existing, key, value)

    
    db.add(existing)
    await db.commit()
    await db.refresh(existing)
    return existing


@router.delete("/{teacher_id}", status_code = status.HTTP_204_NO_CONTENT)
async def delete_teacher(teacher_id: int, db:AsyncSession = Depends(get_async_session)):
    result = await db.execute(select(Teacher).where(Teacher.id == teacher_id))
    teacher = result.scalar_one_or_none()
    if not teacher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    await db.delete(teacher)
    await db.commit()
    return None
