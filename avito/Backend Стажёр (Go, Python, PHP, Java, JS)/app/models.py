from sqlalchemy import Float, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from .database import Base


class Announcement(Base):
    __tablename__ = 'announcements'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    photos = Column(String)
