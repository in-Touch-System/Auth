from typing import Annotated
from app.dto import BaseDTOModel, TokenResponseDTO
from app.validators import phone_number_validator, password_validator, email_validator
from pydantic import AfterValidator

class SignInWithPhoneNumberRequestDTO(BaseDTOModel):
    phone_number: Annotated[str, AfterValidator(phone_number_validator)]


class SignInWithEmailAndPasswordRequestDTO(BaseDTOModel):
    email: Annotated[str, AfterValidator(email_validator)]
    password: Annotated[str, AfterValidator(password_validator)]


class SignInResponseDTO(TokenResponseDTO):
    pass
