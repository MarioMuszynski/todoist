import logging
import os
import requests
from requests.structures import CaseInsensitiveDict


def create_new_task(project_id, task_content, priority, formatted_date):
    logger = logging.getLogger('main_logger')
    try:
        url = "https://api.todoist.com/rest/v1/tasks"
        bearer_token = "Bearer " + os.environ['TODOIST_API_KEY']
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = bearer_token
        headers["Content-Type"] = ""
        body = {
            "content": task_content,
            "due_string": formatted_date,
            "project_id": project_id,
            "priority": priority
        }
        ""
        resp = requests.post(url, headers=headers, data=body, verify=False)
        print(resp.status_code)
        if resp.status_code == 200:
            return 0
        else:
            return 1
        logger.info(task)
    except Exception as e:
        logger.error(e, stack_info=True, exc_info=True)
