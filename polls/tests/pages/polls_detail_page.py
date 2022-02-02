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
