from pydantic import BaseModel

class MangaBase(BaseModel):
    id:         int
    title:      str
    alt_title:  str
    # author:     str

class Manga(BaseModel):
    status:     str
    genres:     list = []
    tags:       list = []

class MangaChapters(MangaBase):
    images:     str