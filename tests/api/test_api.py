import pytest


@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''


@pytest.mark.check
def test_name(user):
    assert user.name == "Olga"


@pytest.mark.check
def test_second_name(user):
    assert user.second_name == "Kostina"
