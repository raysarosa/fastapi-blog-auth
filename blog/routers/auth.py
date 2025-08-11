from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from blog.database import get_session
from blog.models import User
from blog.schemas import TokenLogin, Token
from blog.hashing import Hash
from blog.token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/", response_model=Token)
def login(auth_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: Session = Depends(get_session)):
    # Busca o usuário com base no username
    statement = select(User).where(User.email == auth_data.username)
    user = session.exec(statement).first()

    # Verifica se usuário existe
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials"
        )

    # Verifica se a senha bate com o hash
    if not Hash.verify(auth_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password"
        )
    
    # Se tudo estiver correto, gere um JWT Token e retorne
    access_token = create_access_token(data={"sub": user.email})
    return Token(access_token=access_token, token_type="bearer")

