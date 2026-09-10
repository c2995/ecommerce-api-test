import pytest
from reset_db import  reset

@pytest.fixture(scope="session",autouse=True)
def reset_database():
    reset()
    yield


FLAKY_NODEIDS = {"testcases/test_runner.py::TestRunner::test_case[case63]",
    "testcases/test_runner.py::TestRunner::test_case[case188]"}

def pytest_collection_modifyitems(items):
    for item in items:
        if item.nodeid in FLAKY_NODEIDS:
            item.add_marker(pytest.mark.flaky(reruns=2))
