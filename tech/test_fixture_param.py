import pytest

@pytest.fixture(params=["wang", 24, 180])
def prepare_data(request):
    return request.param

def test_1(prepare_data):
    print(f'testdata:{prepare_data}')