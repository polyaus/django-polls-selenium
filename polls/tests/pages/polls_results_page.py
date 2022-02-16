from polls.tests.pages.base_page import BasePage
from polls.tests.pages.locators import PollsListView


class PagePollsResults(BasePage):
    def check_user_voted(self, text_1, text_2):
        results = self.selenium.find_elements(*PollsListView.RESULTS)
        self.assertEqual(results[0].text, text_1,
                         f"User voted incorrectly, {results[0].text}")
        self.assertEqual(results[1].text, text_2,
                         f"User voted incorrectly, {results[1].text}")
