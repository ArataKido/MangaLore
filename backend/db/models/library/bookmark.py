from backend.db.models.base import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Bookmark(Base):
    __tablename__               = 'bookmark'
    
    id                          = Column(Integer, primary_key=True, index=True)
    manga_id                    = Column(Integer, ForeignKey('manga.id'), primary_key=True)
    user_id                     = Column(Integer, ForeignKey('user.id'), primary_key=True)

    manga                       = relationship('Manga', secondary='bookmark',)
    user                        = relationship('User', secondary='bookmark')
