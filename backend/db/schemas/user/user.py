from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    id:                int
    email:             EmailStr
    nickname:          str
    is_active:         bool
    bookmark_id:       list=[int]
    user_manga_status: list=[int]

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    email: EmailStr
    password:          str

class UserUpdate(UserBase):
    password:          str


