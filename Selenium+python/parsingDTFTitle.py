from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://dtf.ru/')
titles = driver.find_elements_by_class_name("content-header__title")
for title in titles:
    print(title.text)



