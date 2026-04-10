from testit_python_commons.decorators import externalId, displayName
class TestNewsSearchPage:
    @externalId("test_news_search_page")
    @displayName("Поиск новости по слову 'Услуга'")
    def test_news_search(self, search_news):  
        search_news.open()
        search_news.enter_input_search("Услуга")
        search_news.click_cart_news()


       