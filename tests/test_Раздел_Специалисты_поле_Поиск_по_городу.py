from testit_python_commons.decorators import externalId, displayName
class TestDoctorsSearchCity:
    @externalId("test_doctors_search_city")
    @displayName("Поиск врачей по городу")
    def test_doctors_search_city(self, doctors_search_city):  
        doctors_search_city.open()
        doctors_search_city.enter_input_search_city("Волоколамск")
        doctors_search_city.click_button_city()