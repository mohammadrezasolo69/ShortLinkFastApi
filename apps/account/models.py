from sqlalchemy import String, DateTime, BINARY, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from databse import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    username: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False, index=True
    )
    phone_number: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    first_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=False)
    is_staff: Mapped[bool] = mapped_column(default=False)
    is_verify: Mapped[bool] = mapped_column(default=False)
    verify_date: Mapped[DateTime | None] = mapped_column(DateTime, nullable=True)
    avatar: Mapped[BINARY | None] = mapped_column(BINARY, nullable=True)

    logs = relationship(argument="UserLog", back_populates="user")

    def __str__(self):
        return self.username


class UserLog(Base):
    __tablename__ = "users_logs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    date: Mapped[DateTime] = mapped_column(DateTime,default=datetime.utcnow)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))

    user = relationship(argument="User", back_populates="logs")

    def __str__(self):
        return self.user.username
