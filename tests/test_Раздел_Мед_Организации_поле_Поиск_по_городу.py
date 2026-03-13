class TestSearchCity:
    
    def test_search_city(self, medical_organizations_search_city):  
        medical_organizations_search_city.open()
        medical_organizations_search_city.enter_input_search_city("Волоколамск")
        medical_organizations_search_city.click_button_city()