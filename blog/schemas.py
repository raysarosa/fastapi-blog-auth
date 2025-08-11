from typing import Optional, List
from sqlmodel import SQLModel
from pydantic import BaseModel, EmailStr


# -----------------------------
# Entrada: criação de Blog
# -----------------------------
class BlogCreate(BaseModel):
    title: str
    body: str
    user_id: int  # Relaciona o blog com o usuário dono dele


# -----------------------------
# Entrada: criação de Usuário
# -----------------------------
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


# -----------------------------
# Resumo do Blog (sem criador)
# Usado dentro de UserRead
# -----------------------------
class BlogSummary(BaseModel):
    title: str
    body: str

    class Config:
        from_attributes = True


# -----------------------------
# Resumo do User (sem blogs)
# Usado dentro de BlogRead
# -----------------------------
class UserSummary(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True


# -----------------------------
# Saída: mostrar usuário com seus blogs
# -----------------------------
class UserRead(BaseModel):
    name: str
    email: str
    blogs: List[BlogSummary] = []
    
    class Config:
        from_attributes = True


# -----------------------------
# Saída: mostrar blog com seu criador
# -----------------------------
class BlogRead(BaseModel):
    title: str
    body: str
    creator: Optional[UserSummary] = None  # ← evita erro se não vier

    class Config:
        from_attributes = True


# -----------------------------
# Entrada: login de usuário (para gerar token)
# -----------------------------
class TokenLogin(BaseModel):
    username: str
    password: str

# -----------------------------
# Entrada: JWT Token
# -----------------------------
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None