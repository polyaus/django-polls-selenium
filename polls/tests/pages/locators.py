from selenium.webdriver.common.by import By


class PollsListView:
    NAME_QUESTION_IN_LIST = (By.CSS_SELECTOR, ".question_list .question_list__item a")
    NAME_QUESTION = (By.CSS_SELECTOR, ".question .question__text")
    CHOICE = (By.CSS_SELECTOR, ".question label")
