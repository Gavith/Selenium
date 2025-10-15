from selenium import webdriver
from selenium.webdriver.common.by import By

# Start chrome
driver = webdriver.Chrome()

driver.get('https://google.com')

# Grab the texarea (Google search)
google_search = driver.find_element(By.ID, 'APjFqb')

# =============== send_keys() ===================
google_search.send_keys('Selenium')
google_search.submit()


# link = driver.find_element(By.TAG_NAME, "a")
# print(link.get_attribute("href"))  # prints the link’s URL
# username.clear()
