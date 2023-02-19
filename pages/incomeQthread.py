
# -*-coding:utf8 -*-
__author__ = "jermeyjone"
__abc__ = "第一个PySide程序，创建一个窗口"

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
import utils.backend_server_sim as backend 

import pages.userTable as ut
# 主页面信号
class mainSignal(QObject):
    setMainPage= Signal(int)
main_signal = mainSignal()

class thread(QObject):
    def __init__(self, ui, arg=None):
        super(thread, self).__init__(arg)
        self.ui = ui
        backend.init()
    def close_event(self, event):
        print('exit!!!!!!')
