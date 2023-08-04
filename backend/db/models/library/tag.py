from backend.db.models.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Tag(Base):
    __tablename__               = "tag"

    id                          = Column(Integer, primary_key=True, index=True)
    name                        = Column(String, unique=True, index=True)

    manga                       = relationship('Manga', secondary='tag',)