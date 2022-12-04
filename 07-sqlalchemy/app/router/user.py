from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import UserBase
from app.db.database import get_db
from app.db import db_user
from app.schemas import UserDisplay

router = APIRouter(
    prefix='/user',
    tags=['user']
)

# Create user


@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

# Read user

# Update user

# Delete user