from selenium.webdriver.common.by import By

class HomePageConfig:
    ACCEPT_COOKIES = (By.LINK_TEXT, "Accept All")
    COMPANY_MENU = (By.LINK_TEXT, "Company")
    CAREERS_LINK = (By.LINK_TEXT, "Careers")

class CareersPageConfig:
    LOCATIONS = (By.ID, "career-our-location")
    TEAMS = (By.ID, "career-find-our-calling")
    LIFE_AT_INSIDER = (By.CSS_SELECTOR, "div.elementor-element.elementor-element-21cea83.elementor-widget.elementor-widget-heading > div > h2")
    SEE_ALL_TEAMS = (By.LINK_TEXT, "See all teams")
    QA_JOBS_LINK = (By.LINK_TEXT, "Quality Assurance")

class JobPageConfig:
    SEE_ALL_QA_JOBS = (By.LINK_TEXT, "See all QA jobs")
    BROWSE_OPEN_POSITION = (By.ID, "career-position-list")
    POSITION1 = (By.XPATH, "//*[@id='jobs-list']/div/div")
    VIEW_ROLE_BUTTON = (By.LINK_TEXT, "View Role")
    LEVEL_URL = "https://jobs.lever.co/useinsider"

class URLs:
    BASE_URL = "https://useinsider.com/"  

class TimeoutConfig:
    DEFAULT_TIMEOUT = 10  
