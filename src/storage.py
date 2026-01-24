from urllib.parse import urlparse

from sqlalchemy import text

from src.db import get_engine


def is_malware(full_url: str) -> bool:
    parsed = urlparse(full_url)

    hostname_and_port = parsed.netloc
    path = parsed.path
    query_string = parsed.query or None

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
