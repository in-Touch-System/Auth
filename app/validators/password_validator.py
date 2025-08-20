import re

def validate_password(value: str):
    if len(value) < 8:
        raise ValueError("The password is too short")

    if not re.search(r"[A-Fa-f0-9]", value) or not re.search(r"[A-Za-z]", value):
        raise ValueError("Password must contain letters and numbers, hex characters are allowed")

    return value