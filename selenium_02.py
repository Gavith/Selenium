# Finding element like a Pro

# ========== 01. By.ID ===========
# <input id='username' type='text'>

from selenium import webdriver
from selenium.webdriver.common.by import By

# start chrome
driver = webdriver.Chrome()

# go to google.com
driver.get('https://google.com')

# Grab the texarea in google search
element = driver.find_element(By.ID, 'APjFqb')
print(element)


# ========== 02. By.CLASS_NAME ===========

element = driver.find_element(By.CLASS_NAME, 'gLFyf')
print(element)

# ========== 03. By.NAME (name attribute) ===========
element = driver.find_element(By.NAME, 'element_name')

# ========== 04. By.CLASS_NAME ===========
element = driver.find_elemnt(By.CSS_SELECTOR, "div.quote > span.text")

# ========== 05. By.XPATH ===========
element = driver.find_element(By.XPATH, "//span[@class='text']")


# Close browser
driver.quit()
