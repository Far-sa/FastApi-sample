from fastapi import FastAPI
from sqlalchemy.orm import Session
from typing import List

from . import models
from .db import engine
from app.api.v1 import api_router

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(api_router)
