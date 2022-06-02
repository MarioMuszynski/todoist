import logging
import os
import sys
import psutil as psutil
from infi.systray import SysTrayIcon


def start_tray():
    try:
        logger = logging.getLogger('main_logger')
        logger.info("Creating tray icon")
        project_root = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(project_root, 'todoist-logo.ico')
        menu_options = (("Show Logs", None, show_logs),)
        systray = SysTrayIcon(icon_path, "Todoist Tool", menu_options, on_quit=close_everything,
                              default_menu_index=1)
        systray.start()
        logger.info("Tray icon created")
    except Exception as e:
        logger.error(e, stack_info=True, exc_info=True)


def show_logs(systray):
    try:
        logger = logging.getLogger('main_logger')
        logger.info("Opening log file")
        project_root = os.path.dirname(os.path.abspath(__file__))
        log_path = os.path.join(project_root, 'todoist.log')
        logger.info(log_path)
        os.startfile(log_path)
        logger.info("Log file opened")
    except Exception as e:
        logger.error(e, stack_info=True, exc_info=True)


def close_everything(systray):
    try:
        logger = logging.getLogger('main_logger')
        logger.info("Killing processes")
        kill_process("todoist.exe")
        logger.info("Exiting system")
        sys.exit(0)
    except Exception as e:
        logger.error(e, stack_info=True, exc_info=True)


def kill_process(process):
    logger = logging.getLogger('main_logger')
    for proc in psutil.process_iter():
        try:
            if process.lower() in proc.name().lower():
                logger.info("Killing " + str(proc.name()))
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return None


