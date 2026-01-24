import logging
from urllib.parse import urlparse

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from src.db import get_engine

logger = logging.getLogger(__name__)


def is_malware(full_url: str) -> bool:
    parsed = urlparse(full_url)

    hostname_and_port = parsed.netloc
    path = parsed.path
    query_string = parsed.query or None

    try:
        engine = get_engine()

        with engine.connect() as conn:
            result = conn.execute(
                text(
                    """
                    SELECT 1
                    FROM malware_urls
                    WHERE hostname_and_port = :host
                      AND path = :path
                      AND (
                            query_string = :query
                            OR query_string IS NULL
                          )
                    LIMIT 1
                    """
                ),
                {
                    "host": hostname_and_port,
                    "path": path,
                    "query": query_string,
                },
            ).first()

            return result is not None

    except SQLAlchemyError:
        logger.exception(
            "DB error while checking malware URL",
            extra={
                "host": hostname_and_port,
                "path": path,
                "query": query_string,
            },
        )

        # Fallback strategy
        return False
