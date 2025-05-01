from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from src.database import Base

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    link = Column(String)
    author = Column(String)
    views = Column(Integer)
    image_url = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) 