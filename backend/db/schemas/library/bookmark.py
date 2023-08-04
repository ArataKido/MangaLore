from pydantic import BaseModel

class BookmarkBase(BaseModel):
    id:                     int
    manga_id:               int
    user_id:                int

    class Config:
        orm_mode = True