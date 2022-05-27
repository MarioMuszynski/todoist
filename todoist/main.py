import os
import sys

import keyboard
import pyautogui
from PyQt5.QtCore import QCoreApplication, Qt, QDate
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QComboBox, QMainWindow, QApplication, QWidget, QPushButton, QLineEdit, \
    QHBoxLayout, QDateEdit
from todoist_api_python.api import TodoistAPI
import infi.systray
import projects
import tasks


def get_api():
    try:
        todoist_api = TodoistAPI(os.environ['TODOIST_API_KEY'])
        return todoist_api
    except Exception as error:
        print(error)


class MainWindow(QMainWindow):
    def __init__(self):
        print("Initializing")
        try:
            print("Initializing superclass")
            super().__init__()
            print("Superclass initialized")

            # Load config
            # config = configparser.ConfigParser()
            # config.read('config.txt')
            # option_values = config.get('settings', 'option')
            # option_value_list = json.loads(option_values)

            # Get project data
            print("Getting project data")
            global apikey
            apikey = get_api()
            print(apikey)
            global project_list
            project_list = projects.get_all_projects(apikey)

            print("Populating dropdowns")
            # Populate dropdown
            self.combobox1 = QComboBox()
            for item in project_list:
                self.combobox1.addItem(item.name)
            self.combobox2 = QComboBox()
            priorities = ["1", "2", "3", "4"]
            self.combobox2.addItems(priorities)

            # Create objects
            self.buttonCreate = QPushButton('Create', self)
            self.buttonCreate.clicked.connect(self.click_create)
            self.buttonCancel = QPushButton('Cancel', self)
            self.buttonCancel.clicked.connect(self.click_cancel)
            self.textbox = QLineEdit(self)
            self.textbox.setFixedHeight(35)
            self.date_picker = QDateEdit(calendarPopup=True)
            self.date_picker.setDate(QDate.currentDate())
            print("Objects created")

            # Set font sizes
            self.textbox.setFont(QFont('Calibri', 18))
            self.combobox1.setFont(QFont('Calibri', 12))
            self.combobox2.setFont(QFont('Calibri', 12))
            self.date_picker.setFont(QFont('Calibri', 12))
            self.buttonCreate.setFont(QFont('Calibri', 12))
            self.buttonCancel.setFont(QFont('Calibri', 12))
            print("Font size set")

            # Add to layout
            self.layout = QHBoxLayout()
            self.layout.addWidget(self.combobox1)
            self.layout.addWidget(self.combobox2)
            self.layout.addWidget(self.date_picker)
            self.layout.addWidget(self.textbox)
            self.layout.addWidget(self.buttonCreate)
            self.layout.addWidget(self.buttonCancel)
            print("Objects added to layout")

            # Set layout
            self.container = QWidget()
            self.container.setLayout(self.layout)
            self.setCentralWidget(self.container)
            current_mouse_x, current_mouse_y = pyautogui.position()
            self.setGeometry(current_mouse_x, current_mouse_y, 900, 100)
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setWindowFlag(Qt.WindowStaysOnTopHint)
            print("Layout set")
        except Exception as error:
            print(error)

    def click_cancel(self):
        try:
            print("Cancelling")
            self.close()
            print("Application cancelled")
        except Exception as error:
            print(error)

    def click_create(self):
        try:
            print("Creating task")
            selected_project = self.combobox1.currentText()
            priority = self.combobox2.currentText()
            task_date = self.date_picker.date()
            print(task_date)
            formatted_date = task_date.toString('yyyy-MM-dd')
            print(formatted_date)
            task_content = self.textbox.text()
            for item in project_list:
                if item.name == selected_project:
                    project_id = item.id
                    break
            tasks.create_new_task(apikey, project_id, task_content, priority, formatted_date)
            print("Task created")
            self.close()
            print("Application quit")
        except Exception as error:
            print(error)

    def keyPressEvent(self, event):
        try:
            if event.key() == Qt.Key_Escape:
                print("Pressed escape")
                self.close()
                print("Application quit")
        except Exception as error:
            print(error)


global app
global w
while True:
    while True:
        try:
            if keyboard.is_pressed('~'):
                print("Pressed ~")
                app = QApplication(sys.argv)
                print("Application loaded")
                w = MainWindow()
                print("Main window declared")
                w.show()
                print("Window shown")
                app.exec_()
                print("Application run finished")
                w.close()
                QCoreApplication.instance().quit()
                app.closeAllWindows()
                print("Application exited")
        except Exception as error:
            print(error)
