class TestMedicalOrganizationsPage:
    
    def test_medical_organizations (self, medical_organizations):  
        medical_organizations.open()
        medical_organizations.click_chapter_medical()
       