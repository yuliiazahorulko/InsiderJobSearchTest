from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.jobs_page import JobsPage
import logging
from utils.screenshots import take_screenshot


class TestInsiderCareers:
    BASE_URL = "https://useinsider.com/"

    def test_career_flow(self, setup):
        logging.info("Test initializer: testing Insider Careers")
        driver = setup
        try:
            driver.get(self.BASE_URL)
            logging.info(f"Visit useinsider.com and check homepage")
            home_page = HomePage(driver)

            take_screenshot(driver, "step_1_navigate_to_careers")
            home_page.go_to_careers_page()
            logging.info(f"Go to Careers page")

            careers_page = CareersPage(driver)
            careers_page.verify_blocks()
            take_screenshot(driver, "step_2_interact_with_elements")
            logging.info(f"Verify blocks in Careers page")

            careers_page.go_to_qa_jobs()
            take_screenshot(driver, "step_3_go_to_qa_jobs")
            logging.info(f"Go to QA jobs")

            jobs_page = JobsPage(driver)
            jobs_page.filter_jobs()
            jobs_page.verify_jobs()
            take_screenshot(driver, "step_4_filter_jobs")
            logging.info(f"Filter jobs and verify results")

            jobs_page.click_view_role()
            take_screenshot(driver, "step_5_final_step")
            logging.info(f"Click View Role and check redirection")
        except AssertionError as e:
            home_page.take_screenshot("test_career_flow_failure")
            logging.error(f"Error during test: {str(e)}")
            raise e
