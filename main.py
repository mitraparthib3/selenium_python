from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.fedex.com/secure-login/en-us/#/login-credentials")

# results = driver.find_elements(By.XPATH, "//*[@id='b_tween']/span")

driver.implicitly_wait(20)
try:
    username = driver.find_element(By.ID, value="userId")
    password = driver.find_element(By.ID, "password")
    username.send_keys("test")
    password.send_keys("pass")
    login_btn = driver.find_element(By.ID, "login-btn")
    login_btn.click()
    
    print(f"page titile {driver.title}")
    driver.implicitly_wait(5)
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("finally block")
    driver.quit()