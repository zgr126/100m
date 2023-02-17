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
import utils.db as db
import calc.List4_Basic as l4
import pages.recordDetailChildPage as pr

import pyqtgraph as pg

import calc.ReadData as cR

class userDetails(QWidget):
    userDetailsSignal = Signal(int)
    type = '新增'
    user = []
    def __init__(self, user, arg=None):
        super(userDetails, self).__init__(arg)
        self.ui = QUiLoader().load('./ui/recordDetail.ui')
        self.ui.pro.setText(str(user[1]))
        self.ui.userName.setText(str(user[0]))
        self.ui.sTime.setText(str(user[2]))
        self.ui.uTime.setText(str(user[4]))
        self.ui.textBrowser.setText(str(user[5]))

        self.layout =  QVBoxLayout()
        self.ui.page.setLayout(self.layout)
        
        self.childPageData = cR.ReadData()

        self.initPage(4)
        self.ui.t4.clicked.connect(self.t4)
        self.ui.t5.clicked.connect(self.t4)
        self.ui.t6.clicked.connect(self.t4)
        self.ui.t7.clicked.connect(self.t4)
        self.ui.t8.clicked.connect(self.t4)
        self.ui.t9.clicked.connect(self.t9)

        
    def clickTop(self, page):
        # 移除layout
        self.pr.setParent(None)
        self.layout.removeWidget(self.pr)
        self.initPage(page)
    def initPage(self,page):
       
        self.pr = pr.Page(page, self.childPageData)
        print(self.pr)
        self.layout.addWidget(self.pr)
    def t9(self):
        self.stackedWidget.setCurrentIndex(1)
    def t4(self):
        self.stackedWidget.setCurrentIndex(0)