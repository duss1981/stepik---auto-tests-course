from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time




def test(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        a1 = browser.find_element_by_id('num1')
        print (a1.text)        
        
        a2 = browser.find_element_by_id('num2')
        b=int(a1.text)+int(a2.text)
        print(str(b))
        
        select = Select(browser.find_element_by_tag_name("select"))
        select.select_by_value(str(b)) # ищем элемент с текстом "Python"

        
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

       
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


test('http://suninjuly.github.io/selects1.html')

