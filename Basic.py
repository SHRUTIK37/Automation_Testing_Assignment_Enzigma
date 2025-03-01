#install selenium
pip install selenium

from selenium import webdriver
import time


# Initialize WebDriver
driver = webdriver.Chrome()

# Open the NoKodr platform
driver.get("https://app-staging.nokodr.com/")

# Maximize browser window
driver.maximize_window()

# for observe the page
time.sleep(3)

# Close the browser
driver.quit()
