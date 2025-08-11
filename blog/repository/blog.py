from fastapi import HTTPException, status, Response
from sqlmodel import select, Session
from blog import models
from blog.models import Blog
from blog.schemas import BlogCreate


def create(session: Session, blog_data: BlogCreate):
    new_blog = models.Blog(**blog_data.model_dump())  # usamos new_blog porque blog é um Pydantic schema, usado só para validação e entrada de dados e new_blog é um modelo ORM (models.Blog) — é ele que será armazenado no banco de dados via session.add(...)
    session.add(new_blog)
    session.commit()
    session.refresh(new_blog)

    # Carrega o relacionamento manualmente
    session.refresh(new_blog, attribute_names=["creator"])

    return new_blog


def list_all(session: Session):
    """Retorna todos os registros de Blog no banco de dados"""
    blogs = session.exec(select(Blog)).all()

    # Carrega explicitamente o relacionamento creator
    for blog in blogs:
        session.refresh(blog, attribute_names=["creator"])

    return blogs


def get_by_id(session: Session, blog_id: int):
    statement = select(Blog).where(Blog.d == blog_id)
    result = session.exec(statement).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {blog_id} not found")
    return result

def update(session: Session, blog_id: int, blog_data: BlogCreate):
    existing_blog = session.get(Blog, blog_id)   # Busca o blog com aquele id no banco
    if not existing_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {blog_id} not found")
    
    # Atualiza todos os campos dinamicamente
    for key, value in blog_data.model_dump().items():
        setattr(existing_blog, key, value)


    # Salva as alterações no banco de dados
    session.add(existing_blog)
    session.commit()

    # Recarrega os dados atualizados do banco de dados
    session.refresh(existing_blog)
    return existing_blog

def delete(session: Session, blog_id: int):
    blog = session.get(Blog, blog_id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog with id {blog_id} not found")    
    session.delete(blog)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
