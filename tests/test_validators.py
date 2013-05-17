from colander_validators import (
    email,
    url)


def test_url():

    assert url("ixmat.us") == True
    assert url("http://bleh.net") == True
    assert type(url("://ixmat.us")) == str
    assert type(url("ixmat")) == str


def test_email():

    assert email("barney@purpledino.com") == True
    assert email("barney.10.WHATDINO@purple.com") == True
    assert type(email("barney")) == str
    assert type(email("barney@dino")) == str
