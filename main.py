from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Opens a demo form site, fills it, and asserts success message
driver = webdriver.Chrome()

try:
    driver.get("https://demoqa.com/automation-practice-form")

    # Fill in first name
    driver.find_element(By.ID, "firstName").send_keys("Christian")

    # Fill in last name
    driver.find_element(By.ID, "lastName").send_keys("Ogunleye")

    # Fill in email
    driver.find_element(By.ID, "userEmail").send_keys("test@example.com")

    # Fill in mobile number
    driver.find_element(By.ID, "userNumber").send_keys("08146289722")

    # Submit the form
    driver.find_element(By.ID, "submit").click()

    # Wait for and assert the success message
    success = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )

    assert "Thanks for submitting the form" in success.text
    print("Test passed — form submitted successfully")

finally:
    driver.quit()