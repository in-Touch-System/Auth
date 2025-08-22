from app.main import app
from app.dto import (
    SignInWithPhoneNumberRequestDTO,
    SignInWithEmailAndPasswordRequestDTO,
)
from fastapi.testclient import TestClient


client = TestClient(app)


def test_signin_with_phone_number():
    payload = SignInWithPhoneNumberRequestDTO(
        telephone_number="+998901234567",
    )

    response = client.post(
        "/auth/signin/phone",
        data=payload.model_dump_json(),
    )

    assert response.status_code == 200

def test_signin_with_email_and_password():
    payload = SignInWithEmailAndPasswordRequestDTO(
        email="test@gmail.com",
        password="12345678"
    )

    response = client.post(
        "/auth/signin/email",
        data=payload.model_dump_json(),
    )

    data = response.json()

    assert response.status_code == 200
    assert "access_token" in data and "refresh_token" in data
