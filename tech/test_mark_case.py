import pytest

@pytest.mark.ios
def test_add():
    print("添加")

@pytest.mark.win
def test_updtae():
    print("更新")

@pytest.mark.web
def test_webtest():
    print("webtest")

if __name__ == '__main__':
    pytest.main()