from sqlalchemy import text

from src.db import engine


def is_malware(url: str) -> bool:
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT 1 FROM malware_urls WHERE url = :url"),
            {"url": url},
        ).first()
        return result is not None
