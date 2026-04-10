from testit_python_commons.decorators import externalId, displayName
class TestDoctorsSearchPage:
    @externalId("test_doctors_search")
    @displayName("Поиск врачей по названию")
    def test_doctors_search(self, doctors_search):  
        doctors_search.open()
        doctors_search.enter_input_search("Лядов Константин Викторович") 
        doctors_search.click_cart_specialist()