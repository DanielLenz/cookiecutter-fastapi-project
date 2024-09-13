import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

from app.database.conn import get_session
from app.database.models import Base, DBUser
from app.main import app

TEST_DATABASE_URL = "sqlite:///:memory:"

test_engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


@pytest.fixture(scope="session")
def session():
    # Initialize
    Base.metadata.create_all(bind=test_engine)
    db_session = TestingSessionLocal()

    try:
        # Add mock data to mock DB
        mock_users = [
            DBUser(id=1, name="Charlie"),
            DBUser(id=2, name="David"),
        ]

        db_session.bulk_save_objects(mock_users)
        db_session.commit()

        yield db_session

    finally:
        # Teardown
        db_session.close()
        Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(scope="session")
def override_get_session(session):
    def _override_get_session():
        return session

    return _override_get_session


@pytest.fixture
def client(override_get_session):
    # Initialize
    app.dependency_overrides[get_session] = override_get_session

    with TestClient(app) as c:
        yield c
    # Teardown
    app.dependency_overrides.clear()
