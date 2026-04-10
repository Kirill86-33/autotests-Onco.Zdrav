from testit_python_commons.decorators import externalId, displayName
class TestClinicSearch:
    @externalId("test_search_clinic")
    @displayName("Поиск клиники")
    def test_search_clinic(self, doctors_search_clinic):  
        doctors_search_clinic.open()
        doctors_search_clinic.enter_input_search_clinic("Волоколамск")
        doctors_search_clinic.click_button_city()