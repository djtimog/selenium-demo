from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://demoqa.com/automation-practice-form")

    
    driver.find_element(By.ID, "firstName").send_keys("Christian")

    
    driver.find_element(By.ID, "lastName").send_keys("Ogunleye")

    driver.find_element(By.ID, "userEmail").send_keys("test@example.com")

    
    driver.find_element(By.ID, "userNumber").send_keys("08146289722")

    
    driver.find_element(By.ID, "submit").click()

    
    success = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )

    assert "Thanks for submitting the form" in success.text
    print("Test passed: form submitted successfully")

finally:
    driver.quit()