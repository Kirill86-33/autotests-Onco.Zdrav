from testit_python_commons.decorators import externalId, displayName
class TestMedicalSearchPage:
    @externalId("test_medical_organizations_search")
    @displayName("Поиск медицинской организации")
    def test_medical_organizations_search(self, medical_organizations_search):  
        medical_organizations_search.open()
        medical_organizations_search.enter_input_search("Волоколамская больница")
        medical_organizations_search.click_cart_lpu()