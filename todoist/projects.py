import logging


def get_all_projects(todoist_api):
    logger = logging.getLogger('main_logger')
    try:
        logger.info("Getting projects from Todoist")
        project_list = todoist_api.get_projects()
        logger.info(project_list)
        return project_list
    except Exception as e:
        logger.error(e, stack_info=True, exc_info=True)


def get_project_id(todoist_api, project_name):
    logger = logging.getLogger('main_logger')
    try:
        logger.info("Getting id for project " + project_name)
        projects = todoist_api.get_projects()
        for item in projects:
            if item.name == project_name:
                project_id = item.id
                logger.info("Id: " + project_id)
                break
        return project_id
    except Exception as e:
        logger.error(e, stack_info=True, exc_info=True)
