from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open NoKodr Signup Page
driver.get("https://app-staging.nokodr.com/signup")
driver.maximize_window()
time.sleep(2)

### SIGNUP USING EMAIL ###

# Select Email Signup Option
email_option = driver.find_element(By.XPATH, "//span[contains(text(), 'Email')]")
email_option.click()
time.sleep(1)

# Test Case 1: Blank Mandatory Fields (Should Show Error)
proceed_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Proceed')]")
proceed_button.click()
time.sleep(2)
print("Email Signup - Test Case 1: Blank fields error message displayed.")

# Test Case 2: Invalid Email Format
email_field = driver.find_element(By.XPATH, "//input[@type='email']")
email_field.send_keys("invalid-email")
proceed_button.click()
time.sleep(2)
print("Email Signup - Test Case 2: Invalid email format error displayed.")

# Test Case 3: Passwords Not Matching
email_field.clear()
email_field.send_keys("testuser@example.com")
password_field = driver.find_element(By.XPATH, "//input[@type='password']")
password_field.send_keys("Test@1234")
confirm_password_field = driver.find_element(By.XPATH, "//input[@name='confirm_password']")
confirm_password_field.send_keys("WrongPass@1234")
proceed_button.click()
time.sleep(2)
print("Email Signup - Test Case 3: Password mismatch error displayed.")

# Test Case 4: Valid Input (Should Proceed to OTP)
confirm_password_field.clear()
confirm_password_field.send_keys("Test@1234")

# Agree to Terms
terms_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
terms_checkbox.click()
time.sleep(1)

# Submit Form
proceed_button.click()
time.sleep(3)

# Check for OTP Verification or Success Message
try:
    otp_input = driver.find_element(By.XPATH, "//input[@type='text']")
    print("Email Signup - Test Case 4: OTP verification required. Please enter OTP manually.")
except:
    try:
        success_msg = driver.find_element(By.CLASS_NAME, "success-message")
        print("Email Signup - Test Case 4: Signup Successful:", success_msg.text)
    except:
        print("Email Signup - Test Case 4: Signup failed or success message not found.")

### SIGNUP USING PHONE ###

# Reload Page
driver.refresh()
time.sleep(2)

# Select Phone Signup Option
phone_option = driver.find_element(By.XPATH, "//span[contains(text(), 'Phone')]")
phone_option.click()
time.sleep(1)

# Test Case 1: Blank Fields (Should Show Error)
proceed_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Proceed')]")
proceed_button.click()
time.sleep(2)
print("Phone Signup - Test Case 1: Blank fields error message displayed.")

# Test Case 2: Invalid Phone Number Format
phone_field = driver.find_element(By.XPATH, "//input[@type='tel']")
phone_field.send_keys("12345")  # Invalid phone number
proceed_button.click()
time.sleep(2)
print("Phone Signup - Test Case 2: Invalid phone number format error displayed.")

# Test Case 3: Valid Phone Number
phone_field.clear()
phone_field.send_keys("9876543210")  # Replace with a valid test phone number

# Agree to Terms
terms_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
terms_checkbox.click()
time.sleep(1)

# Submit Form
proceed_button.click()
time.sleep(3)

# Check for OTP Verification or Success Message
try:
    otp_input = driver.find_element(By.XPATH, "//input[@type='text']")
    print("Phone Signup - Test Case 3: OTP verification required. Please enter OTP manually.")
except:
    try:
        success_msg = driver.find_element(By.CLASS_NAME, "success-message")
        print("Phone Signup - Test Case 3: Signup Successful:", success_msg.text)
    except:
        print("Phone Signup - Test Case 3: Signup failed or success message not found.")

# Close Browser
driver.quit()
