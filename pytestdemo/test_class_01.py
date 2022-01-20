import pytest


def setup_module():
    print('整个模块.py开始')

def teardown_module():
    print('整个模块.py结束')

def setup_function():
    print('    不在类中的方法的开始')

def teardown_function():
    print('    不在类中方法的结束')

def test_w_one():
    print('        不在类中的方法1')

def test_w_two():
    print('        不在类中的方法2')


class TestClass():
    def setup_class(self):
        print('            类的开始')

    def teardown_class(self):
        print('            类的结尾')

    def setup_method(self):
        print('                函数的开始')

    def teardown_method(self):
        print('                函数的结束')

    def test_one(self):
        x = 'this'
        assert "h6" in x

    def test_two(self):
        x = 'hello'
        assert "hello" == x

    def test_three(self):
        a = 'hello'
        b = 'hello world'
        assert a in b



if __name__ == '__main__':
    pytest.main(["-s", "test_class_01.py"])