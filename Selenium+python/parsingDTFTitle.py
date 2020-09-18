from selenium import webdriver

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

print(return_elements_by_class_and_type("content-header__title", "text"))
print(return_elements_by_class_and_type("content-feed__link", "href"))

driver.close()



