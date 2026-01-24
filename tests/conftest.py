import pytest

from src.migrations import run_migrations


@pytest.fixture(scope="session", autouse=True)
def apply_migrations():
    run_migrations()
