from backend.db.models.base import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref

class User(Base):
    __tablename__   = "user"

    id                      = Column(Integer, primary_key=True, index=True)
    bookmark_id             = Column(Integer, ForeignKey('bookmark.id'), primary_key=True)
    user_manga_status_id    = Column(Integer, ForeignKey('usermangastatus.id'), primary_key=True)

    email                   = Column(String, unique=True, index=True)
    password                = Column(String,)
    nickname                = Column(String)
    is_acitve               = Column(Boolean, default=True)

    bookmark                = relationship('Bookmark', back_populates='user', cascade='all, delete-orphan')
    user_manga_status       = relationship('UserMangaStatus', back_populates='user', cascade='all, delete-orphan')