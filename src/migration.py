from pathlib import Path

from sqlalchemy import text

from src.db import get_engine


def run_migrations():
    engine = get_engine()
    migrations_dir = Path(__file__).parent.parent / "migrations"

    for path in sorted(migrations_dir.glob("*.sql")):
        sql = path.read_text()
        with engine.begin() as conn:
            conn.execute(text(sql))
