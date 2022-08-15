import pytest


@pytest.fixture
def data_3():
    return 3


@pytest.fixture
def wide_use():
    print("\nWide use")