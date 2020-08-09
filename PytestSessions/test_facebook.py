import pytest

@pytest.fixture
def setup():
    print("launch chrome")
    print("login to app")


def test_home():
    print("home test")
    assert True



def test_search():
    print("search test")
    assert True




