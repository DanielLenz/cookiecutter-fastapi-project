import pytest
from sqlalchemy.orm import Session

from app.common.exceptions import NotFoundError
from app.common.interfaces import UserCreate, UserUpdate
from app.logic.users import db_create_user, db_delete_user, db_get_user, db_update_user


def test_create_user(session: Session):
    user = db_create_user(UserCreate(name="Alice"), session=session)

    assert user.name == "Alice"
    assert isinstance(user.id, int)


def test_get_user(session: Session):
    # Mock db contains initial users
    # which we try to retrive here.
    # This happens in the conftest.py
    user = db_get_user(user_id=1, session=session)
    assert user.name == "Charlie"


def test_update_user(session: Session):
    user = db_update_user(user_id=2, user=UserUpdate(name="Daniel"), session=session)

    assert user.name == "Daniel"
    assert user.id == 2


def test_delete_user(session: Session):
    user_for_delete = db_create_user(UserCreate(name="Eve"), session=session)

    deleted_user = db_delete_user(user_id=user_for_delete.id, session=session)

    assert user_for_delete.id == deleted_user.id
    assert user_for_delete.name == deleted_user.name

    with pytest.raises(NotFoundError):
        db_get_user(user_id=user_for_delete.id, session=session)
