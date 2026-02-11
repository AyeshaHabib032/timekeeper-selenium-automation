from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class TimerSelectionPage:

    # Home page
    LETS_FOCUS_BUTTON = (By.CSS_SELECTOR, ".home__cta")

    # Timer Selection page
    START_BUTTON = (By.CSS_SELECTOR, ".idle__start")
    PAUSE_BUTTON = (By.CSS_SELECTOR, ".countdown__icon")
    RESET_BUTTON = (By.XPATH, "//button[text()='Reset']")
    FIFTEEN_BUTTON = (By.XPATH, "//button[text()='15:00']")
    FORTY_FIVE = (By.XPATH, "//button[text()='45:00']")
    

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def lets_focus(self):
        self.driver.find_element(*self.LETS_FOCUS_BUTTON).click()

    def click_start(self):
        self.driver.find_element(*self.START_BUTTON).click()

    def click_pause(self):
        self.driver.find_element(*self.PAUSE_BUTTON).click()

    def click_reset(self):
        self.driver.find_element(*self.RESET_BUTTON).click()

    def click_fifteen_button(self):
        self.driver.find_element(*self.FIFTEEN_BUTTON).click()  

    def click_forty_five_button(self):
        self.driver.find_element(*self.FORTY_FIVE).click()  
        

