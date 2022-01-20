import pytest

@pytest.fixture(scope="session")
def login():
    print("用户登录")
    yield
    print("退出登录")