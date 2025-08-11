from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
    @staticmethod
    def bcrypt(password: str) -> str:         # Recebe string e retorna string
        return pwd_context.hash(password)
    
    def verify(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)