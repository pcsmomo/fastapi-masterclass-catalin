from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from app.routers.schemas import PostBase, PostDisplay
from app.database.database import get_db
from app.database import db_post

router = APIRouter(
    prefix='/post',
    tags=['post']
)


@router.post('')
def create(request: PostBase, db: Session = Depends(get_db)):
    return db_post.create(db, request)
