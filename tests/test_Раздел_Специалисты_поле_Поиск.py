class TestDoctorsSearchPage:
    
    def test_doctors_search(self, doctors_search):  
        doctors_search.open()
        doctors_search.enter_input_search("Волоколамская больница")