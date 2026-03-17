from testit_python_commons.decorators import externalId, displayName
class TestSpecialists:
    @externalId("test_specialists")
    @displayName("Раздел 'Специалисты'")
    def test_specialists (self, chapter_specialists):  
        chapter_specialists.open()
        chapter_specialists.click_chapter_specialists()
       