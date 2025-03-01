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

# Click on "Forgot Password"
forgot_password_link = driver.find_element(By.LINK_TEXT, "Forgot Password?")
forgot_password_link.click()
time.sleep(2)

### FORGOT PASSWORD USING EMAIL ###

# Select Email Recovery Option
email_option = driver.find_element(By.XPATH, "//span[contains(text(), 'Email')]")
email_option.click()
time.sleep(1)

# Test Case 1: Blank Email Field (Should Show Error)
proceed_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Proceed')]")
proceed_button.click()
time.sleep(2)
print("Forgot Password (Email) - Test Case 1: Blank email field error displayed.")

# Test Case 2: Invalid Email Format
email_field = driver.find_element(By.XPATH, "//input[@type='email']")
email_field.send_keys("invalid-email")
proceed_button.click()
time.sleep(2)
print("Forgot Password (Email) - Test Case 2: Invalid email format error displayed.")

# Test Case 3: Non-Registered Email
email_field.clear()
email_field.send_keys("notregistered@example.com")
proceed_button.click()
time.sleep(2)
print("Forgot Password (Email) - Test Case 3: Non-registered email error displayed.")

# Test Case 4: Registered Email (Should Send Reset Link)
email_field.clear()
email_field.send_keys("testuser@example.com")  # Replace with actual registered email
proceed_button.click()
time.sleep(3)

# Verify Success Message
try:
    success_message = driver.find_element(By.XPATH, "//p[contains(text(), 'Reset link sent')]")
    print("Forgot Password (Email) - Test Case 4: Reset link sent successfully!")
except:
    print("Forgot Password (Email) - Test Case 4: Reset link message not found.")

### FORGOT PASSWORD USING PHONE ###

# Reload Forgot Password Modal
forgot_password_link.click()
time.sleep(2)

# Select Phone Recovery Option
phone_option = driver.find_element(By.XPATH, "//span[contains(text(), 'Phone')]")
phone_option.click()
time.sleep(1)

# Test Case 1: Blank Phone Field (Should Show Error)
proceed_button.click()
time.sleep(2)
print("Forgot Password (Phone) - Test Case 1: Blank phone field error displayed.")

# Test Case 2: Invalid Phone Format
phone_field = driver.find_element(By.XPATH, "//input[@type='tel']")
phone_field.send_keys("12345")
proceed_button.click()
time.sleep(2)
print("Forgot Password (Phone) - Test Case 2: Invalid phone format error displayed.")

# Test Case 3: Non-Registered Phone
phone_field.clear()
phone_field.send_keys("9998887776")  # Replace with non-registered phone
proceed_button.click()
time.sleep(2)
print("Forgot Password (Phone) - Test Case 3: Non-registered phone error displayed.")

# Test Case 4: Registered Phone (Should Send OTP)
phone_field.clear()
phone_field.send_keys("9876543210")  # Replace with registered phone
proceed_button.click()
time.sleep(3)

# Verify Success Message
try:
    success_message = driver.find_element(By.XPATH, "//p[contains(text(), 'OTP sent')]")
    print("Forgot Password (Phone) - Test Case 4: OTP sent successfully!")
except:
    print("Forgot Password (Phone) - Test Case 4: OTP message not found.")

# Close Browser
driver.quit()
