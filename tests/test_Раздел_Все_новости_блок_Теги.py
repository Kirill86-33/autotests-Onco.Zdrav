
class TestTegNewsSearchPage:
    
    def test_news_search(self, teg_new):  
        teg_new.open()
        teg_new.click_teg_news()
        teg_new.click_cart_news()
     