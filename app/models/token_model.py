from app.models import BaseModel
from sqlalchemy import String, DateTime, UUID, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column


class TokenModel(BaseModel):
    __tablename__ = "tokens"

    token: Mapped[String] = mapped_column(String)
    expires_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True))

    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("UserModel", back_populates="tokens")
