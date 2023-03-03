from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from .model import Blog
from . import schema


def get_all(db: Session):
    blogs = db.query(Blog).all()
    return blogs


def create(request: schema.Blog, db: Session):
    new_blog = Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


def destroy(id, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return "Blog has been deleted successfully"


def retrieve(id, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"blog with id {id} was not found"}
    return blog


def update(id, request: schema.Blog, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with id {id} not found")
    blog.update({'title': request.title, 'body': request.body},
                synchronize_session=False)
    db.commit()
    return "Blog has been updated successfully"
