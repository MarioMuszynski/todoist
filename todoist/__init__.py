import os
import sys
import logging

import keyboard
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QComboBox, QMainWindow, QApplication, QWidget, QPushButton, QLineEdit, \
    QHBoxLayout, QDateEdit
from todoist_api_python.api import TodoistAPI
from infi.systray import SysTrayIcon

import projects
import systray
import tasks

__version__ = '0.1.0'
