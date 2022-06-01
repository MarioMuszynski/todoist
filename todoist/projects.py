import json
import logging
import os
import requests
from requests.structures import CaseInsensitiveDict


def get_all_projects():
    try:
        logger = logging.getLogger('main_logger')
        logger.info("Getting projects from Todoist")
        url = "https://api.todoist.com/rest/v1/projects"
        bearer_token = "Bearer " + os.environ['TODOIST_API_KEY']
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = bearer_token
        resp = requests.get(url, headers=headers)
        logger.info(resp)
        if resp.status_code == 200:
            data = resp.json()
            project_list = json.load(data)
            return project_list
        else:
            return "Error"
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
