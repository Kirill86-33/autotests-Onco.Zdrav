from testit_python_commons.decorators import externalId, displayName
class TestMedicalOrganizationsPage:
    @externalId("test_medical_organizations")
    @displayName("Раздел 'Медицинские организации'")
    def test_medical_organizations (self, medical_organizations):  
        medical_organizations.open()
        medical_organizations.click_chapter_medical()
       