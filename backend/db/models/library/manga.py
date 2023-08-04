from backend.db.models.base import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Manga(Base):
    __tablename__   = "manga"

    id                         = Column(Integer, primary_key=True, index=True)
    tag_id                     = Column(Integer, ForeignKey('tag.id'), primary_key=True)
    genre_id                   = Column(Integer, ForeignKey('genre.id'), primary_key=True)
    bookmark_id                = Column(Integer, ForeignKey('bookmark.id'), primary_key=True)
    user_manga_status_id       = Column(Integer, ForeignKey('usermangastatus.id'), primary_key=True)

    title                      = Column(String,)
    alt_title                  = Column(String)
    manga_status               = Column(String,)
    images                     = Column(String,)
    
    genre                      = relationship('Genre', back_populates='manga', )
    tag                        = relationship('Tag', back_populates='manga', )
    bookmark                   = relationship('Bookmark', back_populates='manga', cascade='all, delete')
    user_manga_status          = relationship('UserMangaStatus', back_populates='manga', cascade='all, delete')



class UserMangaStatus(Base):
    __tablename__               = 'user_manga_status'

    id                          = Column(Integer, primary_key=True, index=True)
    manga_id                    = Column(Integer, ForeignKey('manga.id'), primary_key=True)
    user_id                     = Column(Integer, ForeignKey('user.id'), primary_key=True)
    status                      = Column(String, default=None)

    manga                       = relationship('Manga', secondary='user_manga_status',)
    user                        = relationship('User', secondary='user_manga_status')