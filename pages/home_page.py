from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.ACCEPT_COOKIES = (By.LINK_TEXT, "Accept All")
        self.COMPANY_MENU = (By.LINK_TEXT, "Company")
        self.CAREERS_LINK = (By.LINK_TEXT, "Careers")
    
    def go_to_careers_page(self):
        try:
            logging.info("Navigating to the Careers page")
            self.wait_for_element(*self.ACCEPT_COOKIES).click()
            self.wait_for_element(*self.COMPANY_MENU).click()
            self.wait_for_element(*self.CAREERS_LINK).click()
        except Exception as e:
            logging.error(f"Failed to navigate to the Careers page: {str(e)}")
            raise e