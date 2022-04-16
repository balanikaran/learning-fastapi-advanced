from sqlalchemy import Boolean, Column, Integer, String
from .database import Base

class Users(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=True)
    username = Column(String, nullable=False)

    published = Column(Boolean, default=True, nullable=False)
    