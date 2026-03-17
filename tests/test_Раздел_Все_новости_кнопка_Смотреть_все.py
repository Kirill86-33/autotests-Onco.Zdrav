from testit_python_commons.decorators import externalId, displayName
class TestButtonSeeAll:
    @externalId("test_see_all")
    @displayName("Кнопка 'Смотреть все'")
    def test_see_all(self, button_see_all):  
        button_see_all.open()
        button_see_all.click_button_see_all()
      