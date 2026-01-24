import os

from sqlalchemy import create_engine

DATABASE_URL = os.getenv("DATABASE_URL")

_engine = None

def get_engine():
    global _engine
    if _engine is None:
        db_url = os.getenv("DATABASE_URL")
        if not db_url:
            raise RuntimeError("DATABASE_URL is not set")
        _engine = create_engine(db_url, echo=True)
    return _engine
