from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlmodel import Session, select
from blog import models, schemas
from blog.models import Blog
from blog.schemas import BlogCreate, BlogRead, TokenData
from blog.database import get_session
from blog.repository import blog as blog_repository
from blog.oauth2 import get_current_user


# Organiza todas as rotas relacionadas à funcionalidade (ex: blog):
# 1. Recebe um modelo Pydantic (ou SQLModel) como input.
# 2. Usa uma sessão do banco.
# 3. Executa comandos: add, commit, get, select, etc.

router = APIRouter(
    prefix='/blog',
    tags=["Blogs"]
)

# 1. Criar DB, um a um
@router.post("/", response_model=schemas.BlogRead)
def create(blog_data: schemas.BlogCreate, session: Session = Depends(get_session),
    current_user: TokenData = Depends(get_current_user)):  # blog é um objeto do tipo schemas.BlogCreate (um schema de entrada com apenas title e body) e .model_dump() transforma esse objeto Pydantic em um dicionário Python
    return blog_repository.create(session, blog_data)


# 2. Listar toda a base de dados
# Usar get_current_user para proteger a rota e permitir que só usuários autenticados (com JWT) possam acessar a rota "blog".
@router.get("/", response_model=list[BlogRead])
def list_all_blogs(session: Session = Depends(get_session),
    current_user: TokenData = Depends(get_current_user)):
    return blog_repository.list_all(session)  # Chama a função do repositório


# 3. Detalhar 'id' específico na DB
@router.get("/{blog_id}", response_model=BlogRead)
def get_blog_by_id(blog_id: int, session: Session = Depends(get_session),
    current_user: TokenData = Depends(get_current_user)):
    return blog_repository.get_by_id(session, blog_id)


# 4. Atualizar 'id' específico na DB
@router.put('/{blog_id}', response_model=BlogRead, status_code=status.HTTP_202_ACCEPTED)
def update_id(blog_id: int, blog_data: BlogCreate, session: Session = Depends(get_session),
    current_user: TokenData = Depends(get_current_user)):
    return blog_repository.update(session, blog_id, blog_data)


# 5. Deletar 'id' específico na DB
@router.delete('/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_id(blog_id: int, session: Session = Depends(get_session),
    current_user: TokenData = Depends(get_current_user)):
    return blog_repository.delete(session, blog_id)