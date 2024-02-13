from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# not  ready yet



class FindPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/women/tops-women/tees-women.html'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(FindPage.URL)

    def try_search(self, field_name):
        # Знаходимо поле, в яке будемо вводити track number відправлення
        search_items = self.driver.find_elements(By.CLASS_NAME, field_name)
        # field_name = 'product-item-link'
        WebDriverWait(self.driver, 10)
        
        first_item = search_items[0]
        # print(first_item.id)
        # print(first_item.text)
        # print(first_item.get_attribute('href'))
        
        sorter = self.driver.find_element(By.ID, 'sorter')
        select = Select(sorter)
        select.select_by_value('price')

        # Вводимо неправильний tracknumber
        #search_parcel_elem.send_keys(tracknumber)

        # Знаходимо кнопку Відстежити
        #btn_elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section/div/div/div[1]/div[2]/div[2]")

        # Емулюємо клік лівою кнопкою мишки
        # btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title

    

