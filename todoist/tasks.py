def create_new_task(todoist_api, project_id, task_content, priority, formatted_date):
    try:
        task = todoist_api.add_task(
            content=task_content,
            project_id=project_id,
            priority=priority,
            due_date=formatted_date
        )
        print(task)
    except Exception as error:
        print(error)
