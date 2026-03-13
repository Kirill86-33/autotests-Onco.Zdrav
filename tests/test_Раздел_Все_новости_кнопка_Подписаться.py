import pytest

class TestButtonSubscribe:
    def test_button_subscribe(self, button_subscribe):
        button_subscribe.open()
        button_subscribe.click_button_subscribe_1()
        button_subscribe.enter_input_email ("test@yandex.ru")
        button_subscribe.click_button_subscribe_2()