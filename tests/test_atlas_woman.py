from testit_python_commons.decorators import externalId, displayName
class TestWomanAtlasOncoPage:
    @externalId("test_woman_chapter_onco_atlas")
    @displayName("Раздел 'Атлас Онко Женщина'")
    def test_woman_chapter_onco_atlas(self, info_woman_onco_atlas):  
        info_woman_onco_atlas.open()
        info_woman_onco_atlas.click_button_woman()
        info_woman_onco_atlas.click_button_img()