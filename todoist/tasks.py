import json
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
        headers["Content-Type"] = "application/json"
        body = {
            "content": task_content,
            "due_string": formatted_date,
            "project_id": project_id,
            "priority": priority
        }
        data = json.dumps(body)
        resp = requests.post(url, headers=headers, data=data, verify=False)
        logger.info(resp.status_code)
        if resp.status_code == 200:
            json_response = resp.json()
            task_id = json_response["id"]
            print(task_id)
            return task_id
        else:
            return 0
    except Exception as e:
        logger.error(e, stack_info=True, exc_info=True)
