def get_all_projects(todoist_api):
    try:
        print("Getting projects from Todoist")
        project_list = todoist_api.get_projects()
        print(project_list)
    except Exception as error:
        print(error)
    return project_list


def get_project_id(todoist_api, project_name):
    try:
        print("Getting id for project " + project_name)
        projects = todoist_api.get_projects()
        for item in projects:
            if item.name == project_name:
                project_id = item.id
                print("Id: " + project_id)
                break
        return project_id
    except Exception as error:
        print(error)
