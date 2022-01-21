import pytest

def test_1(login):
    print("用例1：登录后操作1")

def test_2(login):
    print("用例2：无需登录操作1")

def test_3(login):
    print("用例3：登录后操作2")

if __name__ == '__main__':
    pytest.main()

