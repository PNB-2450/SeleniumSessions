import pytest

def test_login_gmail():
    print("This is demo 2 login function")
    assert 10 + 2 ==12

@pytest.mark.login
def test_m4():
    assert False, "Test case failed"

def test_m5():
    name = "Chanti"
    assert name.upper()==name
@pytest.mark.home
def test_m6():
    assert 'chanti' == 'CHANTI'

def test_m7():
    name = "chanti"
    assert name.upper()=="Chanti"