from fastapi import APIRouter, status, Depends
from typing import List
from sqlalchemy.orm import Session

from . import schema
from ..db import get_db
from . import repository


router = APIRouter(
    tags=["Blogs"],
    prefix="/blog"
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schema.Blog, db: Session = Depends(get_db)):
    return repository.create(request, db)


@router.get("/", response_model=List[schema.ShowBlog], status_code=status.HTTP_200_OK)
def get_all_blogs(db: Session = Depends(get_db)):
    return repository.get_all(db)


@router.get("/{id}", response_model=schema.ShowBlog, status_code=status.HTTP_200_OK)
def get_blog_id(id, db: Session = Depends(get_db)):
    return repository.retrieve(id, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy_blog(id, db: Session = Depends(get_db)):
    return repository.destroy(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schema.Blog, db: Session = Depends(get_db)):
    return repository.update(id, request, db)
