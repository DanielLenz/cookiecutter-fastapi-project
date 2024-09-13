from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
