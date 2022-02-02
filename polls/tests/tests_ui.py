import datetime
from urllib.parse import urljoin

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse

from polls.models import Question
from polls.tests.helpers import build_browser, create_question
from polls.tests.pages.polls_detail_page import PagePollsDetail
from polls.tests.pages.polls_list_page import PagePollsList


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

    def get_url_polls_list(self):
        return urljoin(self.live_server_url, reverse('polls:index'))

    def get_url_polls_detail(self, question_id):
        return urljoin(self.live_server_url, reverse('polls:detail', args=[question_id]))

    def test_one_question_is_created_in_page(self):
        question_1 = create_question(question_text="Test question 1", days=0)

        polls_list_page = PagePollsList(self.selenium, self.get_url_polls_list())
        polls_list_page.check_one_question_is_created_on_page()

        polls_detail_page = PagePollsDetail(self.selenium, self.get_url_polls_detail(question_1.pk))
        polls_detail_page.check_question_1_is_on_page()

    def test_two_questions_is_created_in_page(self):
        question_1 = create_question(question_text="Test question 1", days=0)
        question_2 = create_question(question_text="Test question 2", days=0)
        Question.objects.filter(pk=question_1.pk).update(pub_date=question_1.pub_date+datetime.timedelta(seconds=-1))

        polls_list_page = PagePollsList(self.selenium, self.get_url_polls_list())
        polls_list_page.check_two_questions_is_created_on_page()

        polls_detail_page_1 = PagePollsDetail(self.selenium, self.get_url_polls_detail(question_1.pk))
        polls_detail_page_1.check_question_1_is_on_page()

        polls_detail_page_2 = PagePollsDetail(self.selenium, self.get_url_polls_detail(question_2.pk))
        polls_detail_page_2.check_question_2_is_on_page()
