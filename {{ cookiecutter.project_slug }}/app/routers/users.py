from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.common.exceptions import NotFoundError
from app.common.interfaces import User, UserCreate, UserUpdate
from app.database.conn import get_session
from app.logic.users import db_create_user, db_delete_user, db_get_user, db_update_user

router = APIRouter()


@router.post("/", response_model=User, tags=["Users"])
async def create_user(user: UserCreate, session: Session = Depends(get_session)):
    return db_create_user(user, session)


@router.get("/{user_id}", response_model=User, tags=["Users"])
def get_user(user_id: int, session: Session = Depends(get_session)) -> User:
    try:
        return db_get_user(user_id, session)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="User not found")


@router.put("/{user_id}", response_model=User, tags=["Users"])
async def update_user(
    user_id: int, user: UserUpdate, session: Session = Depends(get_session)
):
    try:
        return db_update_user(user_id, user, session)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="User not found")


@router.delete("/{user_id}", response_model=User, tags=["Users"])
async def delete_user(user_id: int, session: Session = Depends(get_session)):
    try:
        return db_delete_user(user_id, session)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="User not found")
