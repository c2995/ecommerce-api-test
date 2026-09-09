import pytest
from reset_db import  reset

@pytest.fixture(scope="session",autouse=True)
def reset_database():
    reset()
    yield 