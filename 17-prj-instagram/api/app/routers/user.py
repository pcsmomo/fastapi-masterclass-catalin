from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from app.routers.schemas import UserBase, UserDisplay
from app.db.database import get_db
from app.db import db_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)
