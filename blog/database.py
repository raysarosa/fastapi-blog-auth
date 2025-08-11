from sqlmodel import SQLModel, create_engine, Session

# Configura o acesso ao banco de dados:
# 1. Criar o banco de dados automaticamente na inicialização.
# 2. Gerar sessões (que são as "conexões temporárias" com o banco).
# 3. Usar com Depends(get_session) em cada rota (isso é moderno e seguro)

DATABASE_URL = "sqlite:///./blog.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    # Cria uma sessão com o banco de dados usando o engine configurado (sqlite, por exemplo)
    # A sessão é usada para executar queries, inserir, atualizar, deletar dados etc.
    with Session(engine) as session:
        
        # 'yield' faz com que o FastAPI use essa sessão enquanto a rota estiver sendo executada
        # Depois disso, o 'with' automaticamente fecha a sessão (mesmo se der erro)
        yield session