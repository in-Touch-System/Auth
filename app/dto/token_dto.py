from datetime import datetime
from app.dto import BaseDTOModel


class RefreshByRefreshTokenRequestDTO(BaseDTOModel):
    refresh_token: str


class RefreshByRefreshTokenResponseDTO(BaseDTOModel):
    refresh_token: str


class TokenResponseDTO(BaseDTOModel):
    access_token: str
    refresh_token: str
    expired_date: datetime
