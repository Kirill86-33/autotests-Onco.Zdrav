from testit_python_commons.decorators import externalId, displayName
class TestSortPage:
    @externalId("test_sort_page")
    @displayName("Сортировка по названию")
    def test_sort_page(self, sort_by_name ):  
        sort_by_name.open()
        sort_by_name.click_button_sort()
        sort_by_name.click_button_by_name()