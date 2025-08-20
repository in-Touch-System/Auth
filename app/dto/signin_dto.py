from app.dto import BaseDTOModel, TokenResponseDTO


class SignInWithPhoneNumberRequestDTO(BaseDTOModel):
    phone_number: str


class SignInWithEmailAndPasswordRequestDTO(BaseDTOModel):
    email: str
    password: str


class SignInResponseDTO(TokenResponseDTO):
    pass
