import pytest
from api.api_client import ApiClient

@pytest.fixture(scope='session')
def client():

    yield ApiClient()
    
@pytest.fixture(scope='session')
def client():
    api_client = ApiClient()

    try:
        api_client.get("/") 
    except Exception:
        pass 
        
    yield api_client