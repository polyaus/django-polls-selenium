from django.test import TestCase


class BasePage(TestCase):
    def __init__(self, selenium, url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.selenium = selenium
        self.url = url

        self.open()

    def open(self):
        if self.url != self.selenium.current_url:
            self.selenium.get(self.url)
