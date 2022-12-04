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


def get_all_user(db: Session):
    return db.query(DbUser).all()


def get_user(db: Session, id: int):
    # TODO: handle any exceptions
    return db.query(DbUser).filter(DbUser.id == id).first()


def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    # TODO: handle any exceptions
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return 'ok'


def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    # TODO: handle any exceptions
    db.delete(user)
    db.commit()
    return 'ok'
