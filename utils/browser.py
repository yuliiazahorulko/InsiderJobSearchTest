from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService


def get_browser(browser_name):
    if browser_name == "firefox":
        return webdriver.Firefox(service=FirefoxService())
    elif browser_name == "chrome":
        return webdriver.Chrome(service=ChromeService())
    else:
        raise ValueError("Browser not supported")
