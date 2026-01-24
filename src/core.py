import logging

from src.storage import is_malware

logger = logging.getLogger(__name__)

def check_url_safety(full_url: str) -> bool:
    """
    Check if the given URL is malicious by querying the storage module.

    Args:
        full_url (str): The URL to check.
    """
    malware = is_malware(full_url)

    logger.info(
            "URL checked",
            extra={
                "url": full_url,
                "is_malware": malware,

                },
            )

    return {
        "url": full_url,
        "is_malware": malware,
        "safe": not malware,
    }
