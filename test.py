from selenium import webdriver
from selenium.webdriver.chrome.service import Service
 
# Указываем путь к драйверу Chrome 114.0.5735.90
service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
 
# Открываем страницу нашего сайта
driver.get("http://localhost:5500")
 
# Проверяем, что заголовок страницы соответствует ожидаемому
assert driver.title == "O-ZONE"

# Проверяем работу поиска
search_field = driver.find_element(By.CLASS_NAME, 'search-wrapper-input')
search_field.clear()
search_field.send_keys("nintendo")
search_field.submit()
assert "Nintendo Switch" in driver.page_source

# Проверяем работу корзины товаров
search_field.clear()
search_field.submit()
cart_window = driver.find_element(By.ID, 'cart')
cart_window.click()
assert "Корзина" in driver.page_source

# Закрываем браузер
driver.quit()
