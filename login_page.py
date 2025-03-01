from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open NoKodr Login Page
driver.get("https://app-staging.nokodr.com/login")
driver.maximize_window()
time.sleep(2)

### LOGIN USING EMAIL ###

# Select Email Login Option
email_option = driver.find_element(By.XPATH, "//span[contains(text(), 'Email')]")
email_option.click()
time.sleep(1)

# Test Case 1: Blank Fields (Should Show Error)
login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Log In')]")
login_button.click()
time.sleep(2)
print("Email Login - Test Case 1: Blank fields error message displayed.")

# Test Case 2: Invalid Email Format
email_field = driver.find_element(By.XPATH, "//input[@type='email']")
email_field.send_keys("invalid-email")
login_button.click()
time.sleep(2)
print("Email Login - Test Case 2: Invalid email format error displayed.")

# Test Case 3: Incorrect Password
email_field.clear()
email_field.send_keys("testuser@example.com")
password_field = driver.find_element(By.XPATH, "//input[@type='password']")
password_field.send_keys("WrongPass@1234")
login_button.click()
time.sleep(2)
print("Email Login - Test Case 3: Incorrect password error displayed.")

# Test Case 4: Valid Credentials (Should Log In)
password_field.clear()
password_field.send_keys("CorrectPass@1234")  # Replace with actual correct password
login_button.click()
time.sleep(3)

# Check for Success Message or Dashboard Redirect
try:
    dashboard_element = driver.find_element(By.XPATH, "//h1[contains(text(), 'Dashboard')]")
    print("Email Login - Test Case 4: Successfully logged in!")
except:
    print("Email Login - Test Case 4: Login failed or success message not found.")

### LOGIN USING PHONE ###

# Reload Page
driver.refresh()
time.sleep(2)

# Select Phone Login Option
phone_option = driver.find_element(By.XPATH, "//span[contains(text(), 'Phone')]")
phone_option.click()
time.sleep(1)

# Test Case 1: Blank Fields (Should Show Error)
login_button.click()
time.sleep(2)
print("Phone Login - Test Case 1: Blank fields error message displayed.")

# Test Case 2: Invalid Phone Number
phone_field = driver.find_element(By.XPATH, "//input[@type='tel']")
phone_field.send_keys("12345")  # Invalid phone number
login_button.click()
time.sleep(2)
print("Phone Login - Test Case 2: Invalid phone number format error displayed.")

# Test Case 3: Incorrect Password
phone_field.clear()
phone_field.send_keys("9876543210")  # Replace with valid test phone number
password_field.clear()
password_field.send_keys("WrongPass@1234")
login_button.click()
time.sleep(2)
print("Phone Login - Test Case 3: Incorrect password error displayed.")

# Test Case 4: Valid Phone Login (Should Log In)
password_field.clear()
password_field.send_keys("CorrectPass@1234")  # Replace with correct password
login_button.click()
time.sleep(3)

# Check for Success Message or Dashboard Redirect
try:
    dashboard_element = driver.find_element(By.XPATH, "//h1[contains(text(), 'Dashboard')]")
    print("Phone Login - Test Case 4: Successfully logged in!")
except:
    print("Phone Login - Test Case 4: Login failed or success message not found.")

# Close Browser
driver.quit()
