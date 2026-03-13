class TestMedicalSearchPage:
    
    def test_medical_organizations_search(self, medical_organizations_search):  
        medical_organizations_search.open()
        medical_organizations_search.enter_input_search("Волоколамская больница")
        