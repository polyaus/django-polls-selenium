import datetime
from urllib.parse import urljoin

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse

from polls.models import Question
from polls.tests.helpers import build_browser, create_question, create_choice
from polls.tests.pages.polls_detail_page import PagePollsDetail
from polls.tests.pages.polls_list_page import PagePollsList
from polls.tests.pages.polls_results_page import PagePollsResults


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

    def get_url_polls_results(self, question_id):
        return urljoin(self.live_server_url, reverse('polls:results', args=[question_id]))

    def test_create_one_question(self):
        question = create_question(question_text="Test question 1", days=0)

        polls_list_page = PagePollsList(self.selenium, self.get_url_polls_list())
        polls_list_page.check_question_is_created()

        polls_detail_page = PagePollsDetail(self.selenium, self.get_url_polls_detail(question.pk))
        polls_detail_page.check_question_is_created()

    def test_two_questions_is_created_in_page(self):
        question_1 = create_question(question_text="Test question 1", days=0)
        question_2 = create_question(question_text="Test question 2", days=0)
        Question.objects.filter(pk=question_1.pk).update(pub_date=question_1.pub_date+datetime.timedelta(seconds=-1))

        polls_list_page = PagePollsList(self.selenium, self.get_url_polls_list())
        polls_list_page.check_two_questions_is_created_on_page()

        polls_detail_page_1 = PagePollsDetail(self.selenium, self.get_url_polls_detail(question_1.pk))
        polls_detail_page_1.check_question_is_created()

        polls_detail_page_2 = PagePollsDetail(self.selenium, self.get_url_polls_detail(question_2.pk))
        polls_detail_page_2.check_question_2_is_on_page()

    def test_one_question_has_two_choices(self):
        question = create_question(question_text="Test question 1", days=0)
        choice_1 = create_choice(question, "Choice 1_1")
        choice_2 = create_choice(question, "Choice 1_2")

        polls_detail_page = PagePollsDetail(self.selenium, self.get_url_polls_detail(question.pk))
        polls_detail_page.check_question_has_two_choices("Choice 1_1", "Choice 1_2")

    def test_two_questions_have_two_choices_each(self):
        question_1 = create_question(question_text="Test question 1", days=0)
        choice_1_1 = create_choice(question_1, "Choice 1_1")
        choice_1_2 = create_choice(question_1, "Choice 1_2")

        question_2 = create_question(question_text="Test question 2", days=0)
        choice_2_1 = create_choice(question_2, "Choice 2_1")
        choice_2_2 = create_choice(question_2, "Choice 2_2")

        polls_detail_page = PagePollsDetail(self.selenium, self.get_url_polls_detail(question_1.pk))
        polls_detail_page.check_question_has_two_choices("Choice 1_1", "Choice 1_2")

        polls_detail_page = PagePollsDetail(self.selenium, self.get_url_polls_detail(question_2.pk))
        polls_detail_page.check_question_has_two_choices("Choice 2_1", "Choice 2_2")

    def test_user_voted_choice_1(self):
        question = create_question(question_text="Test question 1", days=0)
        choice_1 = create_choice(question, "Choice 1_1")
        choice_2 = create_choice(question, "Choice 1_2")

        polls_detail_page = PagePollsDetail(self.selenium, self.get_url_polls_detail(question.pk))
        polls_detail_page.click_choice(number=1)
        polls_detail_page.click_vote_btn()

        polls_results_page = PagePollsResults(self.selenium, self.get_url_polls_results(question.pk))
        polls_results_page.check_user_voted("Choice 1_1 -- 1 vote", "Choice 1_2 -- 0 votes")

    def test_user_voted_choice_2(self):
        question = create_question(question_text="Test question 1", days=0)
        choice_1 = create_choice(question, "Choice 1_1")
        choice_2 = create_choice(question, "Choice 1_2")

        polls_detail_page = PagePollsDetail(self.selenium, self.get_url_polls_detail(question.pk))
        polls_detail_page.click_choice(number=2)
        polls_detail_page.click_vote_btn()

        polls_results_page = PagePollsResults(self.selenium, self.get_url_polls_results(question.pk))
        polls_results_page.check_user_voted("Choice 1_1 -- 0 votes", "Choice 1_2 -- 1 vote")

    def test_user_not_select_choice_and_clicked_vote_btn(self):
        question = create_question(question_text="Test question 1", days=0)
        choice_1 = create_choice(question, "Choice 1_1")
        choice_2 = create_choice(question, "Choice 1_2")

        polls_detail_page = PagePollsDetail(self.selenium, self.get_url_polls_detail(question.pk))
        polls_detail_page.click_vote_btn()
        polls_detail_page.check_message_user_not_choice_variant()
