from sqlalchemy import Column, Integer, String, Foreign_key
from sqlalchemy.orm import relationship


from ..db import Base


class Blog(Base):
    __tablename__ = "Blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

    user_id = Column(Integer, Foreign_key("Users.id"))

    creator = relationship("User", back_populate="blogs")
