from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .schema import User, ShowUser
from .model import User
from ..db import get_db
from .utils import Hash


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/", response_model=ShowUser)
def create(request: User, db: Session = Depends(get_db)):
    new_user = User(username=request.username,
                    email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{id}", response_model=ShowUser)
def get(id, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not available")

    return user
