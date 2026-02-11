from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from pages.timer_selection_page import TimerSelectionPage

def test_timer_selection(driver):
    page = TimerSelectionPage(driver)
# Open 
    driver.get("https://mike-borges.github.io/TimeKeeper/")

    time.sleep(3)
    page.lets_focus() 
    time.sleep(3)
    page.click_start()
    time.sleep(5)
    page.click_pause()
    time.sleep(3)
    page.click_reset()
    time.sleep(3)
    page.click_fifteen_button()
    time.sleep(3)
    page.click_start()
    time.sleep(3)
    page.click_pause()
    time.sleep(3)
    page.click_reset()
    time.sleep(3)
    page.click_forty_five_button()
    time.sleep(3)
    page.click_start()
    time.sleep(3)
    page.click_pause()
    time.sleep(3)
    page.click_reset()
    time.sleep(3)

