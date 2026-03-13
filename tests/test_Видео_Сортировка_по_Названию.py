class TestSortPage:
    
    def test_sort_page(self, sort_by_name ):  
        sort_by_name.open()
        sort_by_name.click_button_sort()
        sort_by_name.click_button_by_name()