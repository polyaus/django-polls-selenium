import time
from urllib.parse import urljoin

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from polls.tests.helpers import build_browser, create_question
from polls.tests.locators import PollsListView


class SeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = build_browser()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_one_question_created_in_page(self):
        question_1 = create_question(question_text="Test question 1", days=0)

        self.selenium.get(urljoin(self.live_server_url, '/polls/'))

        question_1_in_list = self.selenium.find_element(*PollsListView.NAME_QUESTION_IN_LIST)
        self.assertEqual(question_1_in_list.text, "Test question 1",
                         f"Question is not create in list, {question_1_in_list.text}")
        question_1_in_list.click()

        question_1_text = self.selenium.find_element(*PollsListView.NAME_QUESTION)
        self.assertEqual(question_1_text.text, "Test question 1",
                         f"Question name is wrong, {question_1_text.text}")
