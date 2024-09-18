import pytest
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.jobs_page import JobsPage


class TestInsiderCareers:
    def test_career_flow(self, setup):
        driver = setup

        try:
            # Step 1: Visit https://useinsider.com/ and check homepage
            driver.get("https://useinsider.com/")
            home_page = HomePage(driver)
            assert "Insider" in driver.title

            # Step 2: Go to Careers page
            home_page.go_to_careers_page()

            # Step 3: Verify blocks in Careers page
            careers_page = CareersPage(driver)
            careers_page.verify_blocks()

            # Step 4: Go to QA jobs
            careers_page.go_to_qa_jobs()

            # Step 5: Filter jobs and verify results
            jobs_page = JobsPage(driver)
            jobs_page.filter_jobs()
            jobs_page.verify_jobs()

            # Step 6: Click View Role and check redirection
            jobs_page.click_view_role()
            assert "https://jobs.lever.co/useinsider" in driver.current_url

        except AssertionError as e:
            home_page.take_screenshot("test_career_flow_failure")
            raise e
