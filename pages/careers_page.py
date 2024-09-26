from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.config import CareersPageConfig
import time
import logging


class CareersPage(BasePage):
    def verify_blocks(self):
        try:
            logging.info("Verifying Locations, Teams and Life at Insider blocks")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(CareersPageConfig.LOCATIONS), 
                message="Locations block is not visible"
            )
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(CareersPageConfig.TEAMS), 
                message="TEAMS block is not visible"
            )
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(CareersPageConfig.LIFE_AT_INSIDER), 
                message="Life at Insider block is not visible"
            )
        except Exception as e:
            logging.error(f"Failed to verify Locations, Teams and Life at Insider blocks: {str(e)}")
            raise e

    def go_to_qa_jobs(self):
        try:
            logging.info("Navigating to the QA Jobs page")
            see_all_teams = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(CareersPageConfig.SEE_ALL_TEAMS),
                message="See All Teams link is not clickable"
            )
            self.driver.execute_script("scroll(0, 2800)", see_all_teams)
            time.sleep(5)
            see_all_teams.click()
            
            qa_jobs_link = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(CareersPageConfig.QA_JOBS_LINK),
                message="QA Jobs link is not clickable"
            ) 
            self.driver.execute_script("scroll(0, 4500)", qa_jobs_link)
            time.sleep(10)
            self.driver.execute_script("arguments[0].click();", qa_jobs_link)
        except Exception as e:
            logging.error(f"Failed to navigate to the QA Jobs page: {str(e)}")
            raise e
