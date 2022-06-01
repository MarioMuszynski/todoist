import os
import sys
import logging
import keyboard
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QComboBox, QMainWindow, QApplication, QWidget, QPushButton, QLineEdit, \
    QHBoxLayout, QDateEdit
from todoist_api_python.api import TodoistAPI

# Imports for auto-py-to-exe:
import infi
import infi.systray
import pkg_resources
import psutil

# Imports for project modules:
import projects
import systray
import tasks


class MainWindow(QMainWindow):
    def __init__(self):
        self.date_picker = None
        self.textbox = None
        self.buttonCancel = None
        self.buttonCreate = None
        self.combobox2 = None
        self.combobox1 = None
        try:
            # Initialize superclass
            logger = logging.getLogger('main_logger')
            logger.info("Initializing superclass")
            super().__init__()

            # Set layout for Task window
            logger.info("Setting layout for Task window")
            self.layout_task = QHBoxLayout()
            self.container_task = QWidget()
            self.container_task.setLayout(self.layout_task)
            self.setCentralWidget(self.container_task)
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setWindowFlag(Qt.WindowStaysOnTopHint)
            logger.info("Layout set")

            # Create Task objects
            self.combobox1 = QComboBox()
            self.combobox2 = QComboBox()
            self.buttonCreate = QPushButton('Create', self)
            self.buttonCreate.clicked.connect(self.click_create)
            self.buttonCancel = QPushButton('Cancel', self)
            self.buttonCancel.clicked.connect(self.click_cancel)
            self.textbox = QLineEdit(self)
            self.textbox.setFixedHeight(35)
            self.date_picker = QDateEdit(calendarPopup=True)
            self.date_picker.setDate(QDate.currentDate())

            # Set font sizes
            self.textbox.setFont(QFont('Calibri', 18))
            self.combobox1.setFont(QFont('Calibri', 12))
            self.combobox2.setFont(QFont('Calibri', 12))
            self.date_picker.setFont(QFont('Calibri', 12))
            self.buttonCreate.setFont(QFont('Calibri', 12))
            self.buttonCancel.setFont(QFont('Calibri', 12))

            # Add objects to Task layout
            self.layout_task.addWidget(self.combobox1)
            self.layout_task.addWidget(self.combobox2)
            self.layout_task.addWidget(self.date_picker)
            self.layout_task.addWidget(self.textbox)
            self.layout_task.addWidget(self.buttonCreate)
            self.layout_task.addWidget(self.buttonCancel)
            self.main()

        except Exception as e:
            logger.error(e, stack_info=True, exc_info=True)

    def main(self):
        logger = logging.getLogger('main_logger')
        # Loop waiting for ~ key input to show window
        while True:
            try:
                if keyboard.is_pressed('~'):
                    logger.info("Pressed ~")
                    self.show()
                    self.initUI()
                    app.exec_()
                    self.hide()
            except Exception as e:
                logger.error(e, stack_info=True, exc_info=True)

    def initUI(self):
        try:
            logger = logging.getLogger('main_logger')
            logger.info("Initializing UI ")

            # Get project data
            logger.info("Getting project data")
            global api
            global project_list
            api = TodoistAPI(os.environ['TODOIST_API_KEY'])
            project_list = projects.get_all_projects(api)

            # Populate dropdown
            logger.info("Populating dropdowns")
            self.combobox1.clear()
            self.combobox2.clear()
            for item in project_list:
                self.combobox1.addItem(item.name)
            priorities = ["1", "2", "3", "4"]
            self.combobox2.addItems(priorities)

            # Draw UI at cursor position
            logger.info("Drawing UI")
            screen = app.desktop().screenNumber(app.desktop().cursor().pos())
            logger.info(screen)
            center_point = app.desktop().screenGeometry(screen).center()
            logger.info(center_point)
            self.setGeometry(center_point.x()-450, center_point.y()-50, 900, 100)

        except Exception as e:
            logger.error(e, stack_info=True, exc_info=True)

    def click_cancel(self):
        try:
            logger = logging.getLogger('main_logger')
            logger.info("Cancel pressed")
            self.close()
            logger.info("Window closed")
        except Exception as e:
            logger.error(e, stack_info=True, exc_info=True)

    def click_create(self):
        try:
            logger = logging.getLogger('main_logger')
            logger.info("Creating task")
            selected_project = self.combobox1.currentText()
            priority = self.combobox2.currentText()
            task_date = self.date_picker.date()
            logger.info(task_date)
            formatted_date = task_date.toString('yyyy-MM-dd')
            logging.info(formatted_date)
            task_content = self.textbox.text()
            for item in project_list:
                if item.name == selected_project:
                    project_id = item.id
                    break
            tasks.create_new_task(api, project_id, task_content, priority, formatted_date)
            logger.info("Task created")
            self.close()
            logger.info("Window closed")
        except Exception as e:
            logger.error(e, stack_info=True, exc_info=True)

    def keyPressEvent(self, event):
        try:
            logger = logging.getLogger('main_logger')
            if event.key() == Qt.Key_Escape:
                logger.info("Pressed escape")
                self.close()
                logger.info("Window closed")
        except Exception as e:
            logger.error(e, stack_info=True, exc_info=True)


if __name__ == '__main__':
    # Initialize logging
    log_formatter = logging.Formatter('%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s')
    logger = logging.getLogger('main_logger')
    logger.setLevel(level=logging.INFO)

    project_root = os.path.dirname(os.path.abspath(__file__))
    file_handler = logging.FileHandler("{0}/{1}.log".format(project_root, "todoist"))
    file_handler.setFormatter(log_formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)

    # Start tray
    systray.start_tray()

    # Start QApp
    global app
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
