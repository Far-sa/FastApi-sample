from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..db import Base


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populate="creator")
