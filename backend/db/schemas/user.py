from pydantic import BaseModel


class User(BaseModel):
    email:      str
    id:         int
    nickname:   str
    is_active:  bool
    bookmark_id: list=[int]
    user_manga_status: list=[int]

    class Config:
        orm_mode = True


class UserCreate(User):
    password:   str


