from storage import is_malware

def check_url_safety(full_url: str) -> bool:
    """
    Check if the given URL is malicious by querying the storage module.

    Args:
        full_url (str): The URL to check.
    """
    return not is_malware(url)
