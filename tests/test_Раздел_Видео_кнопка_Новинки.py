from testit_python_commons.decorators import externalId, displayName
class TestButtonNew:
    @externalId("test_button_new")
    @displayName("Кнопка 'Новинки' в разделе видео")
    def test_button_new(self, video_button_new):  
        video_button_new.open()
        video_button_new.click_button_new()