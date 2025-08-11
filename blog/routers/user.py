from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlmodel import Session, select
from blog import models, schemas
from blog.models import User
from blog.schemas import UserCreate, UserRead
from blog.database import get_session
from blog.hashing import Hash
from blog.repository import user as user_repository  # ← novo import


router = APIRouter(
    prefix='/user',
    tags=["Users"]
)


# 1. Criar User
@router.post("/", response_model=schemas.UserRead)
def create_user(user_data: schemas.UserCreate, session: Session = Depends(get_session)):
    return user_repository.create(session, user_data)


# 2. Detalhar User com Base no id
@router.get("/{user_id}", response_model=UserRead)
def show_user(user_id: int, session: Session = Depends(get_session)):
    return user_repository.get_by_id(session, user_id)