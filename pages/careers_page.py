from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time
import logging


class CareersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.LOCATIONS = (By.ID, "career-our-location")
        self.TEAMS = (By.ID, "career-find-our-calling")
        self.LIFE_AT_INSIDER = (By.CSS_SELECTOR, "div.elementor-element.elementor-element-21cea83.elementor-widget.elementor-widget-heading > div > h2")
        self.SEE_ALL_TEAMS = (By.LINK_TEXT, "See all teams")
        self.QA_JOBS_LINK = (By.LINK_TEXT, "Quality Assurance")

    def verify_blocks(self):
        try:
            logging.info("Verifying Locations, Teams and Life at Insider blocks")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.LOCATIONS), 
                message="Locations block is not visible"
            )
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.TEAMS), 
                message="TEAMS block is not visible"
            )
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.LIFE_AT_INSIDER), 
                message="Life at Insider block is not visible"
            )
        except Exception as e:
            logging.error(f"Failed to verify Locations, Teams and Life at Insider blocks: {str(e)}")
            raise e

    def go_to_qa_jobs(self):
        try:
            logging.info("Navigating to the QA Jobs page")
            see_all_teams = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.SEE_ALL_TEAMS),
                message="See All Teams link is not clickable"
            )
            self.driver.execute_script("scroll(0, 2800)", see_all_teams)
            time.sleep(5)
            see_all_teams.click()
            
            qa_jobs_link = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.QA_JOBS_LINK),
                message="QA Jobs link is not clickable"
            ) 
            self.driver.execute_script("scroll(0, 4500)", qa_jobs_link)
            time.sleep(10)
            self.driver.execute_script("arguments[0].click();", qa_jobs_link)
        except Exception as e:
            logging.error(f"Failed to navigate to the QA Jobs page: {str(e)}")
            raise e
