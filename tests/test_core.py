from src.core import check_url_safety

def test_clean_url():
    url = "http://google.com"
    result = check_url_safety(url)

    assert result["url"] == url
    assert result["is_malware"] is False
    assert result["safe"] is True


def test_malware_url():
    url = "http://bad.com/malware"
    result = check_url_safety(url)

    assert result["url"] == url
    assert result["is_malware"] is True
    assert result["safe"] is False


def test_unknown_path_is_safe():
    url = "http://bad.com/other"
    result = check_url_safety(url)

    assert result["is_malware"] is False
    assert result["safe"] is True
