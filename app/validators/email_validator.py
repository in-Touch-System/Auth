import re

def validate_email(value: str) -> str:
    if value is None:
        raise ValueError("email must be required")

    if not re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", value):
        raise ValueError("Некорректный формат email")

    return value