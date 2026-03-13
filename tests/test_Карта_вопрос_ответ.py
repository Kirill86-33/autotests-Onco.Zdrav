import pytest

class TestLeaveForm:
    def test_leave_form(self, card_question_answer):
        card_question_answer.open()
        card_question_answer.enter_name("ТЕСТ ТЕСТ")
        card_question_answer.enter_phone("+73333333333")
        card_question_answer.enter_email("test@yandex.ru")
        card_question_answer.enter_district("Московская область")  
        card_question_answer.enter_comment("ТЕСТОВАЯ ПРОВЕРКА")
        card_question_answer.click_send_button()
        
   
  
