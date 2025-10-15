from selenium import webdriver
from selenium.webdriver.common.by import By

# 01. Start Chrome
driver = webdriver.Chrome()

# 02. Open a website
driver.get("https://quotes.toscrape.com/")

# 03. Find element by their class name
quotes = driver.find_elements(By.CLASS_NAME, "text")

# 04. Print all qoutes
for q in quotes:
	print(q.text)

# 05. Close browser
driver.quit()
