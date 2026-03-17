from testit_python_commons.decorators import externalId, displayName
class TestVideoSearchPage:
    @externalId("test_video_search")
    @displayName("Поиск видео по слову 'Вопросы'")
    def test_video_search(self, video_search_page ):  
        video_search_page.open()
        video_search_page.enter_input_search("Вопросы")
        video_search_page.click_button_section_video()