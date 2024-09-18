from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    ACCEPT_COOKIES = (By.XPATH, "//*[@id='wt-cli-accept-all-btn']")
    COMPANY_MENU = (By.XPATH, "//nav//a[contains(text(), 'Company')]")
    CAREERS_LINK = (By.XPATH, "//a[text()='Careers']")

    def go_to_careers_page(self):
        self.wait_for_element(*self.ACCEPT_COOKIES).click()
        self.wait_for_element(*self.COMPANY_MENU).click()
        self.wait_for_element(*self.CAREERS_LINK).click()
