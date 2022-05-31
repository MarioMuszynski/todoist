import os
import sys
import logging

from infi.systray import SysTrayIcon


def start_tray():
    try:
        logger = logging.getLogger('main_logger')
        logger.info("Creating tray icon")
        project_root = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(project_root, 'todoist-logo.ico')
        menu_options = (("Show Logs", None, show_logs),)
        systray = SysTrayIcon(icon_path, "Example tray icon", menu_options, on_quit=close_everything, default_menu_index=1)
        systray.start()
        logger.info("Tray icon created")
    except Exception as e:
        logger.error(e, stack_info=True, exc_info=True)


def show_logs(systray):
    pass


def close_everything(systray):
    print("Closing through tray")
    sys.exit()
