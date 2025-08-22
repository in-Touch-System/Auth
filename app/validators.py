import re
from typing import Optional


def validate_email_address(email: str) -> Optional[str]:
    pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
    if not pattern.match(email):
        raise ValueError("Invalid email format")
    return email

def validate_password(password: str) -> Optional[str]:
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")
    if not re.search(r"[A-Z]", password):
        raise ValueError("Password must contain at least one uppercase letter")
    if not re.search(r"[a-z]", password):
        raise ValueError("Password must contain at least one lowercase letter")
    if not re.search(r"[0-9]", password):
        raise ValueError("Password must contain at least one digit")
    if not re.search(r"[@$!%*?&]", password):
        raise ValueError("Password must contain at least one special character (@$!%*?&)")
    return password

def validate_phone_number(phone: str) -> Optional[str]:
    pattern = re.compile(r"^\+998\d{9}$")
    if not pattern.match(phone):
        raise ValueError("Phone number must be in format +998XXXXXXXXX")
    return phone
