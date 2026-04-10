from testit_python_commons.decorators import externalId, displayName
class TestBlockTopic:
    @externalId("test_block_topic")
    @displayName("Блок темы в разделе видео")
    def test_block_topic(self, teg_block_topic):  
        teg_block_topic.open()
        teg_block_topic.click_button_block_topic()
        teg_block_topic.click_button_video()
        