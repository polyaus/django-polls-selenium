from selenium.webdriver.common.by import By


class PollsListView:
    NAME_QUESTION_IN_LIST = (By.CSS_SELECTOR, ".question_list .question_list__item a")
    NAME_QUESTION = (By.CSS_SELECTOR, ".question .question__text")
    CHOICE_TEXT = (By.CSS_SELECTOR, ".question label")
    CHOICE_RADIO_BTN = (By.CSS_SELECTOR, "#choice%d")
    BTN_VOTE = (By.CSS_SELECTOR, ".btn_vote")
    RESULTS = (By.CSS_SELECTOR, ".results li")
    MESSAGE_ERROR = (By.CSS_SELECTOR, ".question strong")
