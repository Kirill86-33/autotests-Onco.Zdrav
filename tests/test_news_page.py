from testit_python_commons.decorators import externalId, displayName
class TestButtonNews:
    @externalId("test_news")
    @displayName("Кнопка 'Все новости'")
    def test_news(self, all_news):  
        all_news.open()
        all_news.click_button_news()
   