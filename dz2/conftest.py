import pytest
from datetime import datetime


@pytest.fixture(scope='session', autouse=True)
def set_time():
    start_date = datetime.now()
    yield
    last_date = datetime.now()
    print(last_date - start_date)


@pytest.fixture(scope='function')
def string_list():
    return ['apple', 'banana', 'kiwi']


@pytest.fixture(scope='function')
def string_wasd():
    return 'wasd'


@pytest.fixture(scope='function')
def string_WASD():
    return 'WASD'


@pytest.fixture(scope='function')
def dict_key_string():
    return {'one': 1, 'three': 3, 'two': 2}


@pytest.fixture(scope='function')
def set_items():
    return {'car', 'bike', 'bus'}


@pytest.fixture(scope='function')
def set_items_for_union():
    return {1, 2, 3}


@pytest.fixture(params=[('bus', {'car', 'bike'}), ('car', {'bike', 'bus'}), ('bike', {'car', 'bus'})])
def set_test_params(request):
    return request.param
