import pytest
from utils.browser import get_browser


@pytest.fixture(params=["chrome", "firefox"]) 
def setup(request):
    driver = get_browser(request.param)
    driver.maximize_window()
    yield driver
    driver.quit()
