from testit_python_commons.decorators import externalId, displayName
class TestButtonShowAll:
    @externalId("test_show_all")
    @displayName("Кнопка 'Показать все'")
    def test_show_all(self, button_show_all):  
        button_show_all.open()
        button_show_all.click_button_show_all ()
      