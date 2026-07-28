from datetime import datetime

from sqlalchemy import (
    String,
    Integer,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class ActivityLog(Base):

    __tablename__ = "activity_logs"


    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )


    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )


    action: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )


    description: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )


    user = relationship(
        "User",
        back_populates="activities"
    )