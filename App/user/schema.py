from pydantic import BaseModel
from typing import List

from blogs.schema import ShowBlog


class User(BaseModel):
    username: str
    email: str
    password: str


class ShowUser(BaseModel):
    username: str
    email: str
    blogs = List[ShowBlog] = []

    class Config():
        orm_mode = True
