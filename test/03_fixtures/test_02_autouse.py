import pytest


@pytest.fixture(autouse=True)
def auto():
    print("\n Auto fixture")


def test_01():
    print("test_01 started")


def test_02():
    print("test_02 started")
