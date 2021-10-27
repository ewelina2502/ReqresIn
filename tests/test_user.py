import pytest

from models import user
from models.user import Newuser


def test_get_list():
    users = user
    users.get_list()


def test_single(my_new_user):
    single = user
    single.get_single_user()


def test_create_new_user(my_new_user):
    create = Newuser()
    create.create_user()


@pytest.fixture
def my_new_user():
    new = Newuser()
    return new.create_user()
