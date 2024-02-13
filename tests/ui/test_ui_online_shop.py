from modules.ui.page_objects.find_parcel_novaposhta import FindPage
import pytest
# not  ready yet

@pytest.mark.ui_online_shop
def test_search_sorted_item_page_object():
    # створення об'єкту сторінки
    search_item_page = FindPage()

    # відкриваємо сторінку https://magento.softwaretestingboard.com/women/tops-women/tees-women.html
    search_item_page.go_to()

    # виконуємо спробу знайти товар
    search_item_page.try_search("product-item-link")
    
    # first_item = search_items[0]
        # print(first_item.id)
        # print(first_item.text)
        # print(first_item.get_attribute('href'))
        
        # sorter = self.driver.find_element(By.ID, 'sorter')
        # select = Select(sorter)
        # select.select_by_value('price')

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    # assert search_parcel_page.check_title("Трекінг посилки | Nova Global")

    # Закриваємо браузер
    # search_parcel_page.close()
