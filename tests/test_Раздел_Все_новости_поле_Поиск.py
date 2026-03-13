class TestNewsSearchPage:
    
    def test_news_search(self, search_news):  
        search_news.open()
        search_news.enter_input_search("Услуга")
        search_news.click_cart_news()


       