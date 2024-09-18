from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


class JobsPage(BasePage):
    SEE_ALL_QA_JOBS = (By.XPATH, "//*[@id='page-head']/div/div/div[1]/div/div/a")
    FILTER = (By.XPATH, "//*[@id='career-position-filter']/div/div/div[1]/button/div[2]/span")
    LOCATION_FILTER = (By.XPATH, "//*[@id='filter-by-location']")
    DROPDOWN = (By.XPATH, "//*[@id='top-filter-form']/div[1]/span/span[1]/span/span[2]")
    VALUE = (By.XPATH, "//*[@id='select2-filter-by-location-result-1e86-Istanbul, Turkey']")
    SELECT2DROPDOWN = (By.XPATH, "/html/body/span/span")
    DEPARTMENT_FILTER = (By.XPATH, "//*[@id='filter-by-department']")
    JOB_LIST = (By.XPATH, "//*[@id='jobs-list']/div/div")
    BROWSE_OPEN_POSITION = (By.XPATH, "//*[@id='career-position-list']/div/div/div[1]/h3")
    POSITION1 = (By.XPATH, "//*[@id='jobs-list']/div/div")
    VIEW_ROLE_BUTTON = (By.XPATH, "//*[@id='jobs-list']/div/div/a")

    def filter_jobs(self):
        self.driver.implicitly_wait(40)
        WebDriverWait(self.driver, 20).until(
             EC.element_to_be_clickable(self.SEE_ALL_QA_JOBS),
             message="SEE_ALL_QA_JOBS link is not clickable"
        ).click()
        self.driver.implicitly_wait(40)
        WebDriverWait(self.driver, 100).until(
            EC.visibility_of_element_located(self.LOCATION_FILTER), 
            message="LOCATION_FILTER block is not visible"
        )
        self.driver.implicitly_wait(100)
        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(By.XPATH, '//*[@id="filter-by-department"]').get_attribute('value') == 'Quality Assurance'
        )
        # self.driver.save_screenshot('screenshot.png')
        dropdown_element = self.driver.find_element(By.XPATH, "//*[@id='filter-by-location']")

        select = Select(dropdown_element)
        select.select_by_visible_text("Istanbul, Turkey")
        # self.driver.save_screenshot('screenshot3.png')


    def verify_jobs(self):
        self.driver.execute_script("window.scrollBy(0, 500);")
        browse_open_positions = WebDriverWait(self.driver, 80).until(
            EC.visibility_of_element_located(self.BROWSE_OPEN_POSITION), 
            message="BROWSE_OPEN_POSITION block is not visible"
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(browse_open_positions)
        # self.driver.save_screenshot('screenshot4.png')

        position1 = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.POSITION1), 
            message="POSITION1 block is not visible"
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(position1)
        # self.driver.save_screenshot('screenshot5.png')

        # jobs = self.wait_for_element(*self.JOB_LIST)
        # job_list = WebDriverWait(self.driver, 40).until(
        #     EC.visibility_of_element_located(self.JOB_LIST),
        #     message="JOB_LIST link is not visible"
        # )
        # # Move to the element and click using Actions
        
        # # if not isinstance(jobs, list):
        # #     raise TypeError("Expected a list of elements, but got: {}".format(type(jobs)))
        # actions = ActionChains(self.driver)
        # actions.move_to_element(job)
        

        # print("***")
        # print(job)
        # for job in jobs:
        #     assert "Quality Assurance" in job.text
        #     assert "Istanbul, Turkey" in job.text

        print(f"Text in position1: {position1.text}")
        assert "Quality Assurance" in position1.text
        # self.assert_text_in_element(position1, "Quality Assurance")   

    def click_view_role(self):
        # Locate the element that needs to be hovered over to reveal the button
        position1 = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.POSITION1),
            message="POSITION1 block is not visible"
        )

        # Hover over the position element to reveal the 'view_role' button
        actions = ActionChains(self.driver)
        actions.move_to_element(position1).perform()

        # Now that the view_role button is visible, locate and click it
        view_role = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.VIEW_ROLE_BUTTON),
            message="VIEW_ROLE_BUTTON link is not clickable"
        )

        # Check the href attribute to confirm the URL
        href_value = view_role.get_attribute("href")
        assert "https://jobs.lever.co/useinsider" in href_value, f"Unexpected href: {href_value}"

        # Click the view role button
        view_role.click()

        # Wait for some time or until a condition is met (e.g., the new page is loaded)
        # time.sleep(40)

        # Get window handles
        handles = self.driver.window_handles

        # Switch to the new tab (the last handle in the list is the new tab)
        self.driver.switch_to.window(handles[-1])

        # Validate the URL of the new tab
        current_url = self.driver.current_url
        print(f"Current URL: {current_url}")
        assert "https://jobs.lever.co/useinsider" in current_url