from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import HomePageConfig
import logging


class HomePage(BasePage):
    def go_to_careers_page(self):
        try:
            logging.info("Navigating to the Careers page")
            self.wait_for_element(*HomePageConfig.ACCEPT_COOKIES).click()
            self.wait_for_element(*HomePageConfig.COMPANY_MENU).click()
            self.wait_for_element(*HomePageConfig.CAREERS_LINK).click()
        except Exception as e:
            logging.error(f"Failed to navigate to the Careers page: {str(e)}")
            raise e