from datetime import date
from unittest import TestCase

from todoist.tasks import create_new_task


class Test(TestCase):
    def test_create_new_task(self):
        task_id = create_new_task(2253002703, "Test", "1", "2022-06-02")
        self.assertTrue(task_id > 1)
