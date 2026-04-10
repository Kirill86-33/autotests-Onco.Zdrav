from testit_python_commons.decorators import externalId, displayName
class TestServicePage:
    @externalId("test_chapter_service")
    @displayName("Раздел 'Услуга'")
    def test_chapter_service(self, chapter_service ):  
        chapter_service.open()
        chapter_service.click_chapter_service()
        chapter_service.click_cart_inpatient_care()



    
   
     
        