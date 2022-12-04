from sqlalchemy.orm import Session
from app.schemas import UserBase
from app.db.models import DbUser
from app.db.hash import Hash


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # to receive auto-generated id
    return new_user
