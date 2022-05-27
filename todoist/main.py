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
        self.date_picker = None
        self.textbox = None
        self.buttonCancel = None
        self.buttonCreate = None
        self.combobox2 = None
        self.combobox1 = None
        try:
            # Initialize superclass
            print("Initializing superclass")
            super().__init__()

            # Set layout
            print("Setting layout")
            self.layout = QHBoxLayout()
            self.container = QWidget()
            self.container.setLayout(self.layout)
            self.setCentralWidget(self.container)
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setWindowFlag(Qt.WindowStaysOnTopHint)
            print("Layout set")

            # Create objects
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

            # Add to layout
            self.layout.addWidget(self.combobox1)
            self.layout.addWidget(self.combobox2)
            self.layout.addWidget(self.date_picker)
            self.layout.addWidget(self.textbox)
            self.layout.addWidget(self.buttonCreate)
            self.layout.addWidget(self.buttonCancel)

        except Exception as error:
            print(error)

    def main(self):
        app = QApplication(sys.argv)
        app.exec()
        while True:
            try:
                if keyboard.is_pressed('~'):
                    print("Pressed ~")
                    MainWindow.show()
                    self.initUI()
                    MainWindow.hide()
            except Exception as error:
                print(error)
        self.initUI()

    def initUI(self):
        try:
            # Get project data
            global apikey
            apikey = get_api()
            print(apikey)
            global project_list
            project_list = projects.get_all_projects(apikey)

            # Populate dropdown
            self.combobox1.clear()
            self.combobox2.clear()
            for item in project_list:
                self.combobox1.addItem(item.name)
            priorities = ["1", "2", "3", "4"]
            self.combobox2.addItems(priorities)

            # Draw UI at cursor position
            current_mouse_x, current_mouse_y = pyautogui.position()
            self.setGeometry(current_mouse_x, current_mouse_y, 900, 100)

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


if __name__ == '__main__':
    m = MainWindow()
    m.main()
