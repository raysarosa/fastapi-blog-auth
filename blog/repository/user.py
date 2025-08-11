from fastapi import HTTPException, status
from sqlmodel import Session, select
from blog.models import User
from blog.schemas import UserCreate
from blog.hashing import Hash

def create(session: Session, user_data: UserCreate):
    hashed_password = Hash.bcrypt(user_data.password)
    user_dict = user_data.model_dump()
    user_dict["password"] = hashed_password

    new_user = User(**user_dict)      # desempacotando o dicionário user_data como argumentos nomeados (key=value)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

def get_by_id(session: Session, user_id: int):
    statement = select(User).where(User.id == user_id)
    result = session.exec(statement).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
    return result