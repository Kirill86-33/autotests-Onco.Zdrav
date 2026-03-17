from testit_python_commons.decorators import externalId, displayName
class TestVideoPage:
    @externalId("test_video")
    @displayName("Просмотр видео")
    def test_video(self, video_page):  
        video_page.open()
        video_page.click_button_video()
    