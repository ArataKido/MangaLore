from pydantic import BaseModel


class MangaBase(BaseModel):
    id:                     int
    title:                  str
    alt_title:              str
    images:                 str
    manga_status:           str
    
    bookmark_id:            int
    user_manga_status_id:   int
    genres:                 list = [int]
    tags:                   list = [int]


    class Config:
        orm_mode = True


class UserMangaStatusBase(BaseModel):
    id:                     int
    manga_id:               int
    user_id:                int
    status:                 str

    class Config:
        orm_mode = True