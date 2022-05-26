import os

from todoist_api_python.api import TodoistAPI


class TodoistProjects:

    def get_api(self):
        todoist_api = TodoistAPI(os.environ['TODOIST_API_KEY'])
        return todoist_api

    def get_all_projects(todoist_api):
        try:
            projects = todoist_api.get_projects()
        except Exception as error:
            print(error)
        return projects

    def get_project_id(todoist_api, project_name):
        try:
            projects = todoist_api.get_projects()
            for item in projects:
                if item.name == project_name:
                    project_id = item.id
                    break
            return project_id
        except Exception as error:
            print(error)