from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db import Subject, get_async_session
from app.schemas import SubjectCreate, SubjectRead
from app.users import current_active_user

router = APIRouter(
    prefix = '/subjects',
    tags = ['Subjects'],
    dependencies = [Depends(current_active_user)],

)

@router.post("/", response_model=SubjectRead, status_code=status.HTTP_201_CREATED)
async def create_subject(
    subject: SubjectCreate, db: AsyncSession = Depends(get_async_session)
):
    new_subject = Subject(**subject.model_dump())
    db.add(new_subject)
    await db.commit()
    await db.refresh(new_subject)
    return new_subject


@router.get('/', response_model = list[SubjectRead])
async def get_subjects( db: AsyncSession = Depends(get_async_session)):
    result = await db.execute(select(Subject))
    subjects = result.scalars().all()
    return subjects

@router.get('/{subject_id}', response_model=SubjectRead)
async def get_subject(subject_id: int, db: AsyncSession = Depends(get_async_session)):
    result = await db.execute(select(Subject).where(Subject.id == subject_id))
    subject = result.scalar_one_or_none()

    if not subject:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return subject


@router.put('/{subject_id}', response_model = SubjectRead)
async def update_subject(subject_id: int, updated_data: SubjectCreate, db:AsyncSession = Depends(get_async_session)): 
    result = await db.execute(select(Subject).where(Subject.id == subject_id))
    subject = result.scalar_one_or_none()

    if not subject:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND)
    
    for key, value in updated_data.model_dump().items():
        setattr(subject, key, value)

    db.add(subject)
    await db.commit()
    await db.refresh(subject)
    return subject



@router.delete('/{subject_id}', status_code = status.HTTP_204_NO_CONTENT)
async def delete_subject(subject_id: int, db:AsyncSession = Depends(get_async_session)):
    result = await db.execute(select(Subject).where(Subject.id == subject_id))
    subject = result.scalar_one_or_none()

    if not subject:
        raise HTTPException(status_code=404, details = "not found")
    
    await db.delete(subject)
    await db.commit()
    return None

