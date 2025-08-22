from typing import Annotated
from app.dto import BaseDTOModel
from app.validators import phone_number_validator, password_validator, email_validator
from pydantic import BeforeValidator, AfterValidator


class SignUpWithPhoneNumberRequestDTO(BaseDTOModel):
    phone_number: Annotated[str, AfterValidator(phone_number_validator)]


class SignUpWithEmailAndPasswordRequestDTO(BaseDTOModel):
    email: Annotated[str, AfterValidator(email_validator)]
    password: Annotated[str, BeforeValidator(password_validator)]
    confirm_password:  Annotated[str, BeforeValidator(password_validator)]

    def validate(self):
        if self.password != self.confirm_password:
            raise ValueError("passwords didn't match")
