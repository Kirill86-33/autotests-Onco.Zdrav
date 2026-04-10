from testit_python_commons.decorators import externalId, displayName
class TestMedicalOrganizationsPage:
    @externalId("test_medical_organizations")
    @displayName("Раздел 'Медицинские организации'")
    def test_medical_organizations(self, medical_organizations):
        medical_organizations.open()
        import time
        time.sleep(5)
        print("\n--- PAGE SOURCE (первые 3000 символов) ---")
        print(medical_organizations.driver.page_source[:3000])
        medical_organizations.click_chapter_medical()
        medical_organizations.click_cart_lpu()



      

   
       
       
       