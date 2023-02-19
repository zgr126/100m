
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
import pages.incomeQthread as Qthread

import pages.userTable as ut
# 主页面信号
class mainSignal(QObject):
    setMainPage= Signal(int)
main_signal = mainSignal()

class income(QWidget):
    def __init__(self, ui, arg=None):
        super(income, self).__init__(arg)
        self.ui = ui
        # 实例化需要多线程直接方法的类，里面包含执行方法
        worker_obj = Qthread()
        # 实例化QThread，开启一个新线程对象
        worker_thread = QThread()
        # 将执行方法的类的线程指向转移至新的线程对象
        worker_obj.moveToThread(worker_thread)
        backend.init()
    def close_event(self, event):
        print('exit!!!!!!')
