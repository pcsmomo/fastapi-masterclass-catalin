from sqlalchemy.orm.session import Session
import datetime
from app.routers.schemas import PostBase
from .models import DbPost


def create(db: Session, request: PostBase):
    new_post = DbPost(
        image_url=request.image_url,
        title=request.title,
        content=request.content,
        creator=request.creator,
        timestamp=datetime.datetime.now()
    )
    db.add(new_post)
    db.commit()
    # because db would generate unique ID, and we want to receive it
    db.refresh(new_post)
    return new_post
