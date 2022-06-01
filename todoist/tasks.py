import logging


def create_new_task(todoist_api, project_id, task_content, priority, formatted_date):
    logger = logging.getLogger('main_logger')
    try:
        task = todoist_api.add_task(
            content=task_content,
            project_id=project_id,
            priority=priority,
            due_date=formatted_date
        )
        logger.info(task)
    except Exception as e:
        logger.error(e, stack_info=True, exc_info=True)
