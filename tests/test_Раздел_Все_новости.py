class TestButtonNews:
    
    def test_news(self, all_news):  
        all_news.open()
        all_news.click_button_news()
   