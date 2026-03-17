from testit_python_commons.decorators import externalId, displayName
class TestAtlasOncoPage:
    @externalId("test_chapter_onco_atlas")
    @displayName("Раздел 'Атлас Онко Мужчина'")
    def test_chapter_onco_atlas(self, chapter_onco_atlas):  
        chapter_onco_atlas.open()
        chapter_onco_atlas.click_chapter_onco_atlas()
        chapter_onco_atlas.click_vision_hearing()
        chapter_onco_atlas.click_eye_tumor()