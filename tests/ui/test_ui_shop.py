import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.ui_shop
def test_check_first_element():
    # Створення об'єкту для керування бразуером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   
    # відкриваємо сторінку https://magento.softwaretestingboard.com/women/tops-women/tees-women.html
    driver.get("https://magento.softwaretestingboard.com/women/tops-women/tees-women.html")

    # Знаходимо 'product-item-link'
    search_items = driver.find_elements(By.CLASS_NAME, 'product-item-link')

    # Знаходимо в 'product-item-link' назву першого товару
    first_item = search_items[0]

    # Сортируємо товари за ціною - поле 'price'
    sorter = driver.find_element(By.ID, 'sorter')
    select = Select(sorter)
    select.select_by_value('price')
    
    # Чекаємо поки сторінка перезавантажиться
    # Як вариант: WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'Default welcome msg!'))
    WebDriverWait(driver, 10)
    
    # Знаходимо в 'product-item-link' назву першого товару
    search_items = driver.find_elements(By.CLASS_NAME, 'product-item-link')
    new_first_item = search_items[0]
    
    
    assert new_first_item != first_item


    # Close the browser
    driver.close()