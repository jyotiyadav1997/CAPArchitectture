import pytest

@pytest.mark.smoke
def test_login():
    print("Hello")

@pytest.mark.smoke
def test_login1():
    print("Checkout")

@pytest.mark.regresion
def test_login3():
    print("logout")