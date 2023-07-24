from pydantic import BaseModel


class MangaSchema(BaseModel):
    id:                     int
    title:                  str
    alt_title:              str
    images:                 str
    manga_status:           str
    
    genres:                 list = [int]
    tags:                   list = [int]
    bookmark_id:            int
    user_manga_status_id:   int


    class Config:
        orm_mode = True

class TagSchema(BaseModel):
    id:                     int
    name:                   str

    class Config:
        orm_mode = True


class GenreSchema(BaseModel):
    id:                     int
    name:                   str

    class Config:
        orm_mode = True


class BookmarkSchema(BaseModel):
    id:                     int
    manga_id:               int
    user_id:                int

    class Config:
        orm_mode = True


class UserMangaStatusSchema(BaseModel):
    id:                     int
    manga_id:               int
    user_id:                int
    status:                 str

    class Config:
        orm_mode = True