from modules.ui.page_objects.find_parcel_novaposhta import FindPage
import pytest


@pytest.mark.ui_novaposhta
def test_search_incorrect_tracknumber_page_object():
    # створення об'єкту сторінки
    search_parcel_page = FindPage()

    # відкриваємо сторінку https://novaposhtaglobal.ua/track/
    search_parcel_page.go_to()

    # виконуємо спробу знайти відправлення по номеру
    search_parcel_page.try_search("424242")

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert search_parcel_page.check_title("Трекінг посилки | Nova Global")

    # Закриваємо браузер
    search_parcel_page.close()
