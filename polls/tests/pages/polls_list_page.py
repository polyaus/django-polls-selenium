from polls.tests.pages.base_page import BasePage
from polls.tests.pages.locators import PollsListView


class PagePollsList(BasePage):
    def check_question_is_created(self):
        questions_in_list = self.selenium.find_elements(*PollsListView.NAME_QUESTION_IN_LIST)
        self.assertEqual(len(questions_in_list), 1,
                         f"Len questions is wrong, {len(questions_in_list)}")
        self.assertEqual(questions_in_list[0].text, "Test question 1",
                         f"Question is not create in list, {questions_in_list[0].text}")

    def check_two_questions_is_created_on_page(self):
        questions_in_list = self.selenium.find_elements(*PollsListView.NAME_QUESTION_IN_LIST)
        self.assertEqual(len(questions_in_list), 2,
                         f"Len questions is wrong, {len(questions_in_list)}")
        self.assertEqual(questions_in_list[0].text, "Test question 2",
                         f"Question is not create in list, {questions_in_list[0].text}")
        self.assertEqual(questions_in_list[1].text, "Test question 1",
                         f"Question is not create in list, {questions_in_list[1].text}")
