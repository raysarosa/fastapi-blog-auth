# main.py é o ponto de entrada da aplicação

from fastapi import FastAPI                         # Importa a classe principal FastAPI, usada para criar a aplicação.
from blog.routers.blog import router as blog_router  # Importa o roteador (router) do seu módulo blog.routers e dá o apelido blog_router
from blog.routers.user import router as user_router
from blog.routers.auth import router as auth_router
from blog.database import create_db_and_tables  # Importa a função que cria o banco e as tabelas no SQLite, definida no seu database.py
from contextlib import asynccontextmanager          # Importa um decorador que permite criar funções assíncronas com contexto, necessário para o novo sistema lifespan do FastAPI.

# É o ponto de entrada da aplicação:
# 1. Cria a aplicação FastAPI.
# 2. Inicializa o banco de dados assim que a aplicação começa (substituindo o antigo @app.on_event("startup"))
# 3. Inclui as rotas da aplicação

@asynccontextmanager
async def lifespan(app: FastAPI):      # Define a função especial lifespan que será chamada automaticamente quando a aplicação iniciar e finalizar.
    # Executado ao iniciar a aplicação
    create_db_and_tables()             # Função antes do servidor iniciar: cria o banco e suas tabelas
    yield                              # Yield separa o que acontece antes do servidor iniciar e depois que o servidor for desligado

app = FastAPI(lifespan=lifespan)       # Cria a aplicação FastAPI, passando a função lifespan para cuidar do ciclo de vida do app
 
app.include_router(blog_router)        # Inclui as rotas do módulo blog no seu app principal, deixando a organização limpa e modular.
app.include_router(user_router)
app.include_router(auth_router)




