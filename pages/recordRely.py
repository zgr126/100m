
import numpy as np

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import QTimer, QThread, Signal, Slot
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtUiTools import QUiLoader
import time

import pages.userDetails as ud
import utils.db as db

# 主页面信号
class mainSignal(QObject):
    setMainPage= Signal(int)
main_signal = mainSignal()

class Page(QLayout):
    data = []
    def __init__(self, data,arg=None):
        super(Page, self).__init__(arg)
        self.data = data
        self.addWidget(QLabel('百米基础属性2'))