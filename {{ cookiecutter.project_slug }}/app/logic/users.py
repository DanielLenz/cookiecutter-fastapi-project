from sqlalchemy.orm import Session

from app.common.exceptions import NotFoundError
from app.common.interfaces import User, UserCreate, UserUpdate
from app.database.models import DBUser


def db_create_user(user: UserCreate, session: Session):
    db_user = DBUser(**user.model_dump())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return User(**db_user.__dict__)


def db_get_user(user_id: int, session: Session):
    db_user = session.query(DBUser).filter(DBUser.id == user_id).first()
    if not db_user:
        raise NotFoundError
    return User(**db_user.__dict__)


def db_update_user(user_id: int, user: UserUpdate, session: Session):
    db_user = session.query(DBUser).filter(DBUser.id == user_id).first()
    if not db_user:
        raise NotFoundError
    for key, value in user.model_dump().items():
        setattr(db_user, key, value)
    session.commit()
    session.refresh(db_user)
    return User(**db_user.__dict__)


def db_delete_user(user_id: int, session: Session):
    db_user = session.query(DBUser).filter(DBUser.id == user_id).first()
    if not db_user:
        raise NotFoundError
    session.delete(db_user)
    session.commit()
    return User(**db_user.__dict__)
