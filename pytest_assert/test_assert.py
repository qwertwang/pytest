import pytest

'''
assertEqual(arg1, arg2, msg=None)     #验证arg1=arg2，不等则fail
assertNotEqual(arg1, arg2, mag=None)     #验证arg1!=arg2，相等则fail
assertTrue(expr, msg=None)     #验证expr是True，如果为false，则fail
assertFalse(expr, msg=None)     #验证expr是False，如果为true，则fail
assertisNone(expr, msg=None)     #验证expr是None，不是则fail
assertisNotNone(expr, msg=None)     #验证expr不是None，是则fail
assertin(arg1, arg2, msg=None)     #验证arg1是arg2的子串，不是则fail
assertNotin(arg1, arg2, msg=None)     #验证arg1不是arg2的子串，是则fail
'''

def test_one():
    assert 1 == 1
    assert 1 != 2
    assert (1 < 2) == True
    assert "wang" in "wangzhangyin"
    assert {"name": "wang", "age": 24} == {"name": "wang", "age": 24}

def f():
    return 4

def test_two():
    assert f() > 3



if __name__ == '__main__':
    pytest.main()