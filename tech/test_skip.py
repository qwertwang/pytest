import pytest
import sys

'''
skip：直接跳过
skipif：不符合条件跳过
场景：
    1、调试时不想运行这个用例
    2、标记无法在某些平台上运行的测试功能
    3、当前的外部资源不可用时跳过（如果测试数据是从数据库中取到的，连接数据库的功能如果返回结果未成功就不执行跳过，因为执行也都报错）
    4、在某些版本中执行，其他版本中跳过
解决：
    @pytest.mark.skip跳过这个测试用例，可以加条件skipif，在满足某些条件下才希望通过，否则跳过这个测试。
'''

'''
mark中的xfail
场景：
    1、功能测试尚未实施或尚未修复的错误，当测试通过是尽管预计会失败（标记为pytest.mark.xfail）,它是一个xpass将在测试摘要中报告
    2、你希望测试由于某种情况而就应该失败
解决：
    @pytest.mark.xfail
'''

'''
使用自定义标记mark只执行部分用例
场景：只执行符合要求的某一部分用例
    1、可以吧一个web项目划分多个模块
    
'''
@pytest.mark.skipif(sys.version_info > (3,6), reason='版本大于3.6，不运行')
def test_1():
    print("apple")

def test_2():
    print("ios")
    print(sys.version_info)

@pytest.mark.skip
def test_3():
    print("windows")




# skip\skipif
environment = 'android'
@pytest.mark.skipif(environment = "android1", reason="android平台没有这个功能，只在ios下有")
def test_one():
    print("apple")

def test_two():
    print("android")

@pytest.mark.skipif(sys.version_info < (3,6), reason="3.6版本下不执行，您需要更高的版本")
def test_three():
    print("windows")


# xfail
def brokan_fixture():
    raise Exception("sorry,is broken")

@pytest.mark.xfail
def test_xfail():
    print(brokan_fixture())


# 自定义标签


if __name__ == '__main__':
    pytest.main()