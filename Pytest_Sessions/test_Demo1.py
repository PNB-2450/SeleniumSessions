import pytest

@pytest.mark.home
def test_m1():
    a=5
    b=10
    assert a+1 == b, "a+1 is not equal to b"


@pytest.mark.login
def test_m2():
    a=5
    b=10
    assert a == 5

@pytest.mark.home
def test_m3():
    assert True,  "test passed"

@pytest.mark.login
def test_login_insta():
    print("This is Login function of demo1's Class")
    assert "login" == "login"
