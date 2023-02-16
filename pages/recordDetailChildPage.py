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

import matplotlib
matplotlib.use("Qt5Agg")
import sqlite3

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pyqtgraph as pg

class Page(QWidget):
    userDetailsSignal = Signal(int)
    type = '新增'
    user = []
    p4 = [['左肩',0],['右肩',1],['左肘',1],['右肘',1],['左腕',1],['右腕',1],
    ['左髋',1],['右髋',1],['左膝',1],['右膝',1],['左踝',1],['右踝',1],['重心',1]]
    p567 = [['左肩',0],['右肩',1],['左肘',1],['右肘',1],['左腕',1],['右腕',1],
    ['左髋',1],['右髋',1],['左膝',1],['右膝',1],['左踝',1],['右踝',1]]
    p8 = [['左大臂',0],['右大臂',1],['左小臂',1],['右小臂',1],['左躯干',1],['右躯干',1],
    ['左大腿',1],['右大腿',1],['左小腿',1],['右小腿',1]]
    def __init__(self, user, arg=None):
        super(Page, self).__init__(arg)
        self.ui = QUiLoader().load('./ui/recordDetail.ui')
        self.ui.pro.setText(str(user[1]))
        self.ui.userName.setText(str(user[0]))
        self.ui.sTime.setText(str(user[2]))
        self.ui.uTime.setText(str(user[4]))
        self.ui.textBrowser.setText(str(user[5]))

        b = QVBoxLayout()
        self.ui.page.setLayout(b)
        print('ss')
        
        widget = Window(l4.draw())
        b.addWidget(widget)
    def changePage(self, page):
        #第一个单选组
        rbt1 = QRadioButton(window)
        rbt1.move(0, 0)
        rbt1.setText("选项0")
        rbt2 = QRadioButton(window)
        rbt2.move(0, 20)
        rbt2.setText("选项1")
        rbt3 = QRadioButton(window)
        rbt3.move(0, 40)
        rbt3.setText("选项2")
        btg1=QButtonGroup()#创建一个按钮组
        btg1.addButton(rbt1,0)#将单选按钮添加到按钮组，组成单选组。
        btg1.addButton(rbt2,1)
        btg1.addButton(rbt3,2)
        btg1.buttonClicked.connect(butClicked)#添加事件

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
