class TestVideoSearchPage:
    
    def test_video_search(self, video_search_page ):  
        video_search_page.open()
        video_search_page.enter_input_search("Вопросы")
        video_search_page.click_button_section_video()