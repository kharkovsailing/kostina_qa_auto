import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

# This test checks the page sorting function ('price' option)
# url main_link = "https://magento.softwaretestingboard.com/women/tops-women/tees-women.html"
url = "https://magento.softwaretestingboard.com/women/tops-women/tees-women.html"
items = 'product-item-link'

@pytest.mark.ui_shop
def test_check_first_element():
    # Створення об'єкту для керування бразуером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   
    # відкриваємо сторінку https://magento.softwaretestingboard.com/women/tops-women/tees-women.html
    driver.get(url)

    # Знаходимо 'product-item-link'
    search_items = driver.find_elements(By.CLASS_NAME, items)

    # screenshot of the current page
    # now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%m.%s")
    # name_screenshot = 'screenshot_' + now_date + '.png'
    # driver.save_screenshot(name_screenshot)
    
    # Знаходимо в 'product-item-link' назву першого товару
    first_item = search_items[0]

    # Сортируємо товари за ціною - поле 'price'
    sorter = driver.find_element(By.ID, 'sorter')
    select = Select(sorter)
    select.select_by_value('price')
    
    # Чекаємо поки сторінка перезавантажиться
    # Як вариант: WebDriverWait(driver, 10)
    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'Click “Write for us” link in the footer to submit a guest post'))
    
    
    # Знаходимо в 'product-item-link' назву першого товару
    search_items = driver.find_elements(By.CLASS_NAME, items)
    new_first_item = search_items[0]
    
    # screenshot of the current page
    #driver.save_screenshot(name_screenshot)
    
    assert new_first_item != first_item


    # Close the browser
    driver.close()