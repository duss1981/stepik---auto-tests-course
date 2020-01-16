from selenium import webdriver
import time
import os 




def test(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
       
        
        input1=browser.find_element_by_xpath('//*[@name="firstname"]')
        input1.send_keys('Ivan')  
                
        input2=browser.find_element_by_xpath('//*[@name="lastname"]')
        input2.send_keys('Ivanov')  
        
        input3=browser.find_element_by_xpath('//*[@name="email"]')
        input3.send_keys('Ivan@mail.ru')  
        
        element=browser.find_element_by_xpath('//*[@type="file"]')
        
        current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
        file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
        element.send_keys(file_path)
        
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

       
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


test('http://suninjuly.github.io/file_input.html')

