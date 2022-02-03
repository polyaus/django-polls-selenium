from polls.tests.pages.base_page import BasePage
from polls.tests.pages.locators import PollsListView


class PagePollsDetail(BasePage):
    def check_question_1_is_on_page(self):
        question_text = self.selenium.find_element(*PollsListView.NAME_QUESTION)
        self.assertEqual(question_text.text, "Test question 1",
                         f"Question name is wrong, {question_text.text}")

    def check_question_2_is_on_page(self):
        question_text = self.selenium.find_element(*PollsListView.NAME_QUESTION)
        self.assertEqual(question_text.text, "Test question 2",
                         f"Question name is wrong, {question_text.text}")

    def check_question_has_two_choices(self, text_1, text_2):
        choices_text = self.selenium.find_elements(*PollsListView.CHOICE)
        self.assertEqual(len(choices_text), 2,
                         f"Len choices is wrong, {len(choices_text)}")
        self.assertEqual(choices_text[0].text, text_1,
                         f"Question name is wrong, {choices_text[0].text}")
        self.assertEqual(choices_text[1].text, text_2,
                         f"Question name is wrong, {choices_text[1].text}")
