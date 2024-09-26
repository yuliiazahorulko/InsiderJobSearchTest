import pytest
import logging
from utils.browser import get_browser
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

logging.basicConfig(
    filename='test_log.log', 
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  
    datefmt='%Y-%m-%d %H:%M:%S'  
)

logger = logging.getLogger()


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logger.info("Begin of Testing")
    yield
    logger.info("Testing is finished")


@pytest.fixture(params=["chrome", "firefox"])
def setup(request):
    logger.info(f"Run test in {request.param} browser")  
    driver = get_browser(request.param)
    driver.maximize_window()
    yield driver
    driver.quit()
    logger.info(f"End test run in {request.param} browser")
