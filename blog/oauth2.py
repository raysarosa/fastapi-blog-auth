import jwt
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from blog import token, schemas



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")  # onde o token é gerado

app = FastAPI()


def get_current_user(token_data: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token.verify_token(token_data, credentials_exception)