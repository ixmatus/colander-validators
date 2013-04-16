from colander_validators import url


def test_url():

    assert url("ixmat.us") == True
    assert url("http://bleh.net") == True
    assert type(url("://ixmat.us")) == str
    assert type(url("ixmat")) == str
