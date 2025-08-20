import re

def validate_phone_number(value: str) -> str:
    if value is None:
        raise ValueError("phone number must be required")

    if not re.fullmatch(r"\+?\d{10,15}", value):
        raise ValueError("The phone number is incorrect, it must contain 10-15 digits")

    return value
