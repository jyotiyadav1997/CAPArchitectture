import pytest
import sys

@pytest.mark.skip
def test_login():
    print("Test")

@pytest.mark.xfail
def test_payment():
    assert False
    print("Payment Marker")

@pytest.mark.skipif(sys.version_info <(3,9),reason="python version not supported")
def test_payment():
    print("Payment Hello")