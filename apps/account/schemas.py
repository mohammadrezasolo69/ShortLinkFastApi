from pydantic import BaseModel, constr, HttpUrl
from datetime import datetime


class UserSchema:
    class UserBase(BaseModel):
        username: str
        phone_number: str = constr(pattern="")
        first_name: str | None
        last_name: str | None
        avatar: HttpUrl | None

    class UserCreate(UserBase):
        password: str

    class UserDetail(UserBase):
        id: int
        is_active: bool
        is_staff: bool
        is_verify: bool
        verify_date: datetime | None

        class Config:
            orm_mode = True

    class UserList(UserBase):
        id: int
        is_active: bool

        class Config:
            orm_mode = True


class UserLogSchema:
    class UserLogBase(BaseModel):
        pass

    class UserLogCreate(UserLogBase):
        user_id: int

    class UserLogDetail(UserLogBase):
        id:int
        user: UserSchema.UserBase
        date:datetime

        class Config:
            orm_mode = True

    class UserLogList(UserLogBase):
        id:int
        username: UserSchema.UserBase.username
        date:datetime

        class Config:
            orm_mode = True
