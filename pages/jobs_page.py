from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import logging


class JobsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.SEE_ALL_QA_JOBS = (By.LINK_TEXT, "See all QA jobs")
        self.BROWSE_OPEN_POSITION = (By.ID, "career-position-list")
        self.POSITION1 = (By.XPATH, "//*[@id='jobs-list']/div/div")
        self.VIEW_ROLE_BUTTON = (By.LINK_TEXT, "View Role")

    def filter_jobs(self):
        try:
            logging.info("Filtering QA Jobs in Turkey")
            self.driver.implicitly_wait(40)
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.SEE_ALL_QA_JOBS),
                message="SEE_ALL_QA_JOBS link is not clickable"
            ).click()
            self.driver.implicitly_wait(100)
            WebDriverWait(self.driver, 100).until(
                lambda driver: driver.find_element(By.ID, 'filter-by-department').get_attribute('value') == 'Quality Assurance'
            )
            dropdown_element = self.driver.find_element(By.ID, "filter-by-location")
            option_to_select = "Istanbul, Turkey"
            self.driver.execute_script("arguments[0].value = arguments[1];", dropdown_element, option_to_select)
            self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", dropdown_element)
            time.sleep(10)
            dropdown_element1 = self.driver.find_element(By.ID, "filter-by-department")
            option_to_select2 = "Quality Assurance"
            self.driver.execute_script("arguments[0].value = arguments[1];", dropdown_element1, option_to_select2)
            self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", dropdown_element1)
            time.sleep(10)
        except Exception as e:
            logging.error(f"Failed to filter QA Jobs in Turkey: {str(e)}")
            raise e

    def verify_jobs(self):
        try:
            logging.info("Verifying QA Jobs in Turkey")
            self.driver.execute_script("window.scrollBy(0, 500);")
            browse_open_positions = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.BROWSE_OPEN_POSITION), 
                message="BROWSE_OPEN_POSITION block is not visible"
            )
            actions = ActionChains(self.driver)
            actions.move_to_element(browse_open_positions)
            position1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.POSITION1), 
                message="POSITION1 block is not visible"
            )
            actions = ActionChains(self.driver)
            actions.move_to_element(position1)
            print(f"Text in position1: {position1.text}")
            assert "Quality Assurance" in position1.text
        except Exception as e:
            logging.error(f"Failed to verify QA Jobs in Turkey: {str(e)}")
            raise e
        
    def click_view_role(self):
        try:
            logging.info("Clicking 'View Role' for QA Jobs in Turkey")
            position1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.POSITION1),
                message="POSITION1 block is not visible"
            )
            actions = ActionChains(self.driver)
            actions.move_to_element(position1).perform()
            view_role = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.VIEW_ROLE_BUTTON),
                message="VIEW_ROLE_BUTTON link is not clickable"
            )
            time.sleep(10)
            view_role.click()
            handles = self.driver.window_handles 
            self.driver.switch_to.window(handles[-1])
            time.sleep(10)
            current_url = self.driver.execute_script("return window.location.href;")
            print(f"Current URL: {current_url}")
            assert "https://jobs.lever.co/useinsider" in current_url
        except Exception as e:
            logging.error(f"Failed to click 'View Role' for QA Jobs in Turkey: {str(e)}")
            raise e
