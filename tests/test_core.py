from src.core import check_url

def test_clean_url():
    assert check_url("http://google.com") is True
