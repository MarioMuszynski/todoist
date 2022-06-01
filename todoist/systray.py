import os
import sys

from infi.systray import SysTrayIcon


def start_tray():
    try:
        print("Creating tray icon")
        project_root = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(project_root, 'todoist-logo.ico')
        menu_options = (("Options", None, show_options),)
        systray = SysTrayIcon(icon_path, "Example tray icon", menu_options, on_quit=close_everything, default_menu_index=1)
        systray.start()
        print("Tray icon created")
    except Exception as error:
        print(error)


def show_options(systray):
    pass


def close_everything(systray):
    print("Closing through tray")
    sys.exit()
