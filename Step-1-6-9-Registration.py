#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
	link = "http://suninjuly.github.io/registration2.html"
	#browser = webdriver.Chrome()
	browser = webdriver.Firefox()
	browser.get(link)
	# Ваш код, который заполняет обязательные поля
	for i in ['first','second','third']:
		browser.find_element(By.XPATH,'//input[@class="form-control '+i+'" and @required]').send_keys(i)
		time.sleep(1)
	# Отправляем заполненную форму
	button = browser.find_element(By.CSS_SELECTOR, "button.btn")
	button.click()
	time.sleep(1)
	welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
	welcome_text = welcome_text_elt.text
	assert "Congratulations! You have successfully registered!" == welcome_text

finally:
	time.sleep(10)
	browser.quit()
