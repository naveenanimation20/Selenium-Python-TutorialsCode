import pytest

def test_m4():
    assert False

@pytest.mark.home
def test_m5():
    assert 100 == 100

def test_m6():
    assert "naveen" == "NAVEEN"

@pytest.mark.home
def test_login_gmail():
    assert "admin" == "admin"