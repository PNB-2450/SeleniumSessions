import pytest


def test_m4():
    assert False, "Test case failed"
@pytest.mark.home
def test_m5():
    name = "Chanti"
    # login -assert name.upper()==name
    assert name.upper()=="CHANTI"

def test_m6():
    assert 'chanti' == 'CHANTI'

@pytest.mark.login
def test_login_fb():
    print("this is from demo 3")
    assert True