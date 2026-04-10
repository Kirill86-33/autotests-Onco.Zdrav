from testit_python_commons.decorators import externalId, displayName
class TestTegNewsSearchPage:
    @externalId("test_news_search")
    @displayName("Поиск новости по тегу")
    def test_news_search(self, teg_new):  
        teg_new.open()
        teg_new.click_teg_news()
        teg_new.click_cart_news()
     