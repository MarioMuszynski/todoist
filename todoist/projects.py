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
        resp = requests.get(url, headers=headers, verify=False)
        logger.info(resp)
        if resp.status_code == 200:
            project_list = resp.json()
            return project_list
        else:
            return None
    except Exception as e:
        logger.error(e, stack_info=True, exc_info=True)
