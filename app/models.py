from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, text
from .database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=True)
    username = Column(String, nullable=False)

    published = Column(Boolean, server_default="TRUE", nullable=False)

    createdat = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"), nullable=False)