from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

from selenium.webdriver.common.action_chains import ActionChains
import time


class CareersPage(BasePage):
    LOCATIONS = (By.XPATH, "//*[@id='career-our-location']/div/div/div/div[1]/h3")
    TEAMS = (By.XPATH, "//*[@id='career-find-our-calling']/div/div/div[2]")
    LIFE_AT_INSIDER = (By.XPATH, "//h2[text()='Life at Insider']")
    SEE_ALL_TEAMS = (By.XPATH, "//*[@id='career-find-our-calling']/div/div/a")
    QA_JOBS_LINK = (By.XPATH, "//*[@id='career-find-our-calling']/div/div/div[2]/div[12]/div[2]/a/h3")

    def verify_blocks(self):
        # Explicit wait for each block element to ensure they are visible before asserting
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LOCATIONS), 
            message="Locations block is not visible"
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TEAMS), 
            message="Locations block is not visible"
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LIFE_AT_INSIDER), 
            message="Life at Insider block is not visible"
        )

    def go_to_qa_jobs(self):
        # Wait for 'See All Teams' to be clickable
        see_all_teams = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.SEE_ALL_TEAMS),
            message="See All Teams link is not clickable"
        )
        # Move to the element and click using Actions
        actions = ActionChains(self.driver)
        actions.move_to_element(see_all_teams).click().perform()
        # Wait for QA Jobs link to be clickable
        qa_jobs_link = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.QA_JOBS_LINK),
            message="QA Jobs link is not clickable"
        )
        # Move to the element and click using Actions
        actions.move_to_element(qa_jobs_link).click().perform()
