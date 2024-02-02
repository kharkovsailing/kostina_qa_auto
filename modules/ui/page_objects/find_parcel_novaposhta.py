from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class FindPage(BasePage):
    URL = 'https://novaposhtaglobal.ua/track/'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(FindPage.URL)

    def try_search(self, tracknumber):
        # Знаходимо поле, в яке будемо вводити track number відправлення
        search_parcel_elem = self.driver.find_element(By.TAG_NAME, "input")

        # Вводимо неправильний tracknumber
        search_parcel_elem.send_keys(tracknumber)

        # Знаходимо кнопку Відстежити
        btn_elem = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section/div/div/div[1]/div[2]/div[2]")

        # Емулюємо клік лівою кнопкою мишки
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title

    

