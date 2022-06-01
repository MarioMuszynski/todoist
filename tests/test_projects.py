from unittest import TestCase

from todoist.projects import get_all_projects


class Test(TestCase):
    def test_get_all_projects(self):
        result = get_all_projects()
        print(result)
        self.fail()
