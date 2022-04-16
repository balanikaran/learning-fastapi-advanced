from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # default value
    rating: Optional[int] = None  # fully optional value default Null


class UserBase(BaseModel):
    firstname: str
    username: str
    lastname: Optional[str]


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(BaseModel):
    username: str
    createdat: datetime

    class Config:
        orm_mode = True