from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.common.interfaces import DBUser, User, UserCreate

router = APIRouter()

TAGS = ["Users"]


@router.post("/", response_model=User, tags=TAGS)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = DBUser(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return User(**db_user.__dict__)


@router.get("/{user_id}", response_model=User, tags=TAGS)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return User(**db_user.__dict__)
