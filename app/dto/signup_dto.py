from app.dto import BaseDTOModel
from app.validators import (
    validate_email,
    validate_password,
    validate_phone_number,
)

class SignUpWithPhoneNumberRequestDTO(BaseDTOModel):
    phone_number: str

    def validate(self):
        validate_phone_number(self.phone_number)


class SignUpWithEmailAndPasswordRequestDTO(BaseDTOModel):
    email: str
    password: str
    confirm_password: str

    def validate(self):
        validate_email(self.email)
        validate_password(self.password)

        if self.password != self.confirm_password:
            raise ValueError("passwords didn't match")
