from app.main import app
from app.dto import (
    SignUpWithPhoneNumberRequestDTO,
    SignUpWithEmailAndPasswordRequestDTO,
)
from fastapi.testclient import TestClient


client = TestClient(app)


def test_signup_with_phone_number():
    payload = SignUpWithPhoneNumberRequestDTO(
        phone_number="+998901234567"
    )

    response = client.post(
        "/auth/signup/phone",
        data=payload.model_dump_json()
    )

    assert response.status_code == 201

def test_signup_with_email_and_password():
    payload = SignUpWithEmailAndPasswordRequestDTO(
        email="test@gmail.com",
        password="12345678@.",
        confirm_password="12345678@.",
    )

    response = client.post(
        "/auth/signup/email",
        data=payload.model_dump_json()
    )

    assert response.status_code == 201
