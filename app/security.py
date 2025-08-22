from app.config import settings
from app.consts import TokenType
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_token(
    data: dict,
    token_type: str = TokenType.ACCESS.value,
    expires_delta: timedelta | None = None
):
    to_encode = data.copy()
    expire = datetime.now(tz=timezone)

    if token_type == TokenType.REFRESH.value:
        expire += expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    if token_type == TokenType.ACCESS.value:
        expire += expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)

def decode_access_token(token: str):
    try:
        return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError:
        return None
