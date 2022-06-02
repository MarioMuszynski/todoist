from datetime import date
from unittest import TestCase

from todoist.tasks import create_new_task


class Test(TestCase):
    def test_create_new_task(self):
        formatted_date = date.today().toString('yyyy-MM-dd')
        create_new_task(2253002703, "Test", "1", formatted_date)
        self.fail()
