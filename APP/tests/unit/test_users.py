
from allocation.domain.model import Users


def test_adding_to_a_invalid_usertype():
    user = Users("username1", "p@121213", 1)      
    assert user.usertype == 15


def test_adding_to_a_invalid_password():
    user = Users("username1", "######", 1)      
    assert user.password ==""

def test_adding_to_a_invalid_username():
    user = Users("username1", "p@121213", 1)      
    assert user.username =="abcfalse"