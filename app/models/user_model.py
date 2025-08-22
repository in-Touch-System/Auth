from app.models import BaseModel
from sqlalchemy import (
    String,
    Index,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

class UserModel(BaseModel):
    __tablename__ = "users"

    phone_number: Mapped[String] = mapped_column(String, unique=True, nullable=True, index=True)
    email: Mapped[String] = mapped_column(String, unique=True, nullable=True, index=True)
    password: Mapped[String] = mapped_column(String)

    first_name: Mapped[String] = mapped_column(String, nullable=True)
    middle_name: Mapped[String] = mapped_column(String, nullable=True)
    last_name: Mapped[String] = mapped_column(String, nullable=True)

    __table_args__ = (
        Index(
            "idx_user_phone_number_email",
            "phone_number",
            "email",
        ),
    )
