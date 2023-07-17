from backend.db.models.base import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id          = Column(Integer, primary_key=True, index=True)
    email       = Column(String, unique=True, index=True)
    password    = Column(String,)
    is_acitve   = Column(Boolean, default=True)


class Manga(Base):
    __tablename__ = "manga"

    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String,)
    alt_title   = Column(String)
    status      = Column(String,)

class Tag(Base):
    __tablename__ = "tags"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String, unique=True, index=True)

class Genre(Base):
    __tablename__ = "genres"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String, unique=True, index=True)


class MangaTagGenre(Base):
    __tablename__ = 'manga_tag_genre'
    manga_id    = Column(Integer, ForeignKey(Manga.id), primary_key=True) 
    tag_id      = Column(Integer, ForeignKey(Tag.id), primary_key=True)
    genre_id    = Column(Integer, ForeignKey(Genre.id), primary_key=True)