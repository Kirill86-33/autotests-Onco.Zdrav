from testit_python_commons.decorators import externalId, displayName
class TestLpu:
    @externalId("test_button_lpu")
    @displayName("Кнопка 'ЛПУ'")
    def test_button_lpu(self, button_lpu):  
        button_lpu.open()
        button_lpu.click_button_lpu ()
       