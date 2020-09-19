from selenium import webdriver
import json

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://dtf.ru/')

def return_elements_by_class_and_type(className, type):
    result = []
    elementsList = driver.find_elements_by_class_name(className)
    if type == "text":
         for element in elementsList:
            result.append(element.text)
    if type == "href":
        for element in elementsList:
            result.append(element.get_attribute('href'))

    return result

try:
    text = return_elements_by_class_and_type("content-header__title", "text")
    href = return_elements_by_class_and_type("content-feed__link", "href")
finally: driver.close()

json_result = json.dumps(text, href)
print(json_result)


