import pytest


@pytest.fixture
def data_1():
    return 1


@pytest.fixture
def print_hello():
    print("\nHello")


def test_data_01(data_1, print_hello):
    assert data_1 == 1


def test_data_02(data_2):
    assert data_2 == 2


def test_data_03(data_3):
    assert data_3 == 3
