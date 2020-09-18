from selenium import webdriver
driver = webdriver.Chrome('/usr/local/bin/chromedriver')

driver.get('https://vk.com/')
driver.find_element_by_id("index_email").send_keys("login")
driver.find_element_by_id("index_pass").send_keys("password")
driver.find_element_by_id("index_login_button").click()

