import pytest
import sys


@pytest.mark.skip(reason="Skipped test example")
def test_skip():
    pass


@pytest.mark.skipif(sys.version_info > (3, 5), reason="required version more than 3.5")
def test_skip_if():
    pass


@pytest.mark.xfail(reason="Wrong comparison", strick=True)
def test_fail_comparison():
    assert 1 == 0


@pytest.mark.xfail(raieses=(AssertionError, TimeoutError))
def test_fail_exception():
    raise AssertionError
