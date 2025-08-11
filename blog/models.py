from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
# Define como a tabela do banco de dados vai ser estruturada:
# 1. Cria a tabela blogs no banco.
# 2. Define o que é uma coluna (id, title, body).

class Blog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    body: str
    user_id: int = Field(foreign_key="user.id") # Criação de nova coluna que terá relação com blogs [Relação 1:N (1 usuário pode ter N blogs)]

    # Cria a ligação automática com a tabela User e existe um campo chamado blogs que se conecta de volta 
    creator: Optional["User"] = Relationship(back_populates="blogs")


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    password: str

    # Cria relação com Blog
    blogs: list["Blog"] = Relationship(back_populates="creator")      # Cria um campo blogs, que será uma lista com os blogs criados por esse usuário