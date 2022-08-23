import os
import pytest
from unittest import mock

@pytest.fixture
def test_fixture():
    return "fixture!!"

# this will mock the os.listdir with return value "test1"
@mock.patch("os.listdir", mock.MagicMock(return_value="test1"))
def test1():
    print()
    print("from test1: ", os.listdir())
    assert "test1" == os.listdir()
    
# another way to mock os.listdir with return value "test2"
# first argument will be the mock of oslist
@mock.patch("os.listdir")
def test2(mock_listdir, test_fixture):
    mock_listdir.return_value = "test2"
    print("from test2: ", os.listdir())
    print("test_fixture: ", test_fixture)
    assert "test2" == os.listdir()


@mock.patch("os.listdir")
class Test():
    def not_decorated_and_not_tested(self):
        assert False
    def test3(self, mock_listdir):
        mock_listdir.return_value = "test3"
        assert "test3" == os.listdir()
        

# python3 -m pytest -s -rx pytest_practise/6_patch_decorator.py