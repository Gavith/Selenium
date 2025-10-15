# login_automation.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# -------------------------
# Config (change if you want)
URL = "https://the-internet.herokuapp.com/login"
USERNAME = "tomsmith"         # test user for this demo site
PASSWORD = "SuperSecretPassword!"  # test password for this demo site
# -------------------------

def main():
    # 1) start browser (visible)
    driver = webdriver.Chrome()  # if you want headless later, we can add options

    try:
        # 2) open page
        driver.get(URL)

        # 3) find username + password inputs
        user_input = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        pass_input = driver.find_element(By.ID, "password")

        # 4) type creds
        user_input.clear()
        user_input.send_keys(USERNAME)
        pass_input.clear()
        pass_input.send_keys(PASSWORD)

        # 5) click login
        login_btn = driver.find_element(By.CSS_SELECTOR, "button.radius")
        login_btn.click()

        # 6) wait for result message to appear and print it
        message = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.ID, "flash"))
        )
        print("Result message (raw):")
        print(message.text.strip())

        # 7) optional: take screenshot
        driver.save_screenshot("login_result.png")
        print("Saved screenshot -> login_result.png")

    except Exception as e:
        print("Got an error:", type(e).__name__, e)
    finally:
        # short pause so you can watch the result before closing
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    main()
