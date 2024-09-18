import os


def take_screenshot(driver, step_name):
    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    driver.save_screenshot(f"{screenshots_dir}/{step_name}.png")
