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
import matplotlib
matplotlib.use("Qt5Agg")
import sqlite3

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pyqtgraph as pg

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
        
        self.initPage(4)

    def clickTop(self, page):
        # 移除layout
        self.pr.setParent(None)
        self.layout.removeWidget(self.pr)
        self.initPage(page)
    def initPage(self,page):
       
        self.pr = pr.Page(page)
        widget = Window(l4.draw())
        self.layout.addWidget(widget)
        self.ui.page.
        self.pr.changePage(page)

class Window(QWidget):
    def __init__(self, AccXYZArr):
        super().__init__()
        # 设置下尺寸
        self.resize(440,340)
        # 添加 PlotWidget 控件
        self.plotWidget_ted = pg.PlotWidget(self)
        # 设置该控件尺寸和相对位置
        self.plotWidget_ted.setGeometry(QtCore.QRect(20,20,400,300))

        # 仿写 mode1 代码中的数据
        # 生成 300 个正态分布的随机数
        self.data1 = AccXYZArr[:,3,0].tolist()
        self.plotWidget_ted.setYRange(-1,1)
        self.plotWidget_ted.setLabel("left","value",units='V')
        self.plotWidget_ted.setLabel("bottom","Timestamp",units='us')
        self.plotWidget_ted.setTitle('hello title')
        self.plotWidget_ted.setBackground((255, 255, 255))
        self.curve1 = self.plotWidget_ted.plot(self.data1, name="mode1")