import pytest


@pytest.fixture
def fixt(request):
    print("\nBegin in fixt")
    print(f"Call from {request.function.__name__}")
    yield
    print("\nRolling back in fixt")


def test_01(fixt):
    print("\n test_01 started")
