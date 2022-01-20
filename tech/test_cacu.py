from tech.caculate import *
import pytest


def test_add():
    assert add(1, 2) == 3

def test_add_xiao():
    assert add(1.1, 2) == 3





if __name__ == '__main__':
    pytest.main()