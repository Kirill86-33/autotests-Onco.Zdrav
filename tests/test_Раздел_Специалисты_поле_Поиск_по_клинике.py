class TestClinicSearch:
    
    def test_search_clinic(self, doctors_search_clinic):  
        doctors_search_clinic.open()
        doctors_search_clinic.enter_input_search_clinic("Волоколамск")
        doctors_search_clinic.click_button_clinic()