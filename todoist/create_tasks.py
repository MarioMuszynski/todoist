def create_new_task(todoist_api, project_id,task_content,priority):
    try:
        task = todoist_api.add_task(
            content=task_content,
            project_id=project_id,
            priority=priority
        )
        print(task)
    except Exception as error:
        print(error)

