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
# import calc.List4_Basic as l4
import calc.main2 as cm
import utils.QFlowLayout as uQ
# import matplotlib
# matplotlib.use("Qt5Agg")
# import sqlite3

# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
# import matplotlib.pyplot as plt
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
    def __init__(self, page, data, arg=None):
        super(Page, self).__init__(arg)
        self.data = data
        self.addWidget(page)

    def addWidget(self, page):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        print(page)
        if page == 4:
            self.layout.addWidget(self.page4())
        #     self.layout.addWidget(self.changePage(4))
        # btnGroup = self.changePage()
    # def changePage(self, page):
    #     rbt4 = QRadioButton("选项3",window)
    #     rbt4.move(100, 0)
    #     rbt5 = QRadioButton("选项4",window)
    #     rbt5.move(100, 20)
    #     rbt6 = QRadioButton("选项5",window)
    #     rbt6.move(100, 40)
    #     btg2=QButtonGroup()#创建一个按钮组
    #     btg2.addButton(rbt4,3)#将单选按钮添加到按钮组，组成单选组。
    #     btg2.addButton(rbt5,4)
    #     btg2.addButton(rbt6,5)
    #     btg2.buttonClicked.connect(butClicked)#添加事件
    def page4(self):
        

        layout = uQ.FlowLayout()
        # layout = QHBoxLayout()
        # layout.columnMinimumWidth(450)
        wid = QGroupBox()
        wid.setLayout(layout)
        options = cm.Show4(-1,self.data)
        # w= Window({'data':x1,
        #     'title': 'ind点xz面位移图(俯视)',
        #     'yAxix': ['z axis','帧率']
        #     })
        for i in options:
            w = Window(i)
            layout.addWidget(w)
            w.setStyleSheet('''
                QGroupBox {
                    margin-top: 1ex;
                }
                QGroupBox:enabled {
                    border: 3px solid green;
                }
                QGroupBox::title {
                    subcontrol-origin: margin;
                    left: 1ex;
                }''')
            print(w)
        container_layout = QVBoxLayout()
        listW = QListWidget()
        listW.setLayout(container_layout)
        wid.setStyleSheet('''
        QGroupBox {
            margin-top: 1ex;
        }
        QGroupBox:enabled {
            border: 3px solid green;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 1ex;
        }''')
        container_layout.addWidget(wid)
        # container_layout.addStretch()
        # l = QWidget()
        qscrollarea = QtWidgets.QScrollArea()
        qscrollarea.setGeometry(QRect(50,100,600,500))
        qscrollarea.setWidgetResizable(True)
        qscrollarea.setWidget(listW)
        return qscrollarea
class Window(QWidget):
    def __init__(self, options):
        super().__init__()
        # 设置下尺寸
        self.resize(440,340)
        # 添加 PlotWidget 控件
        self.plotWidget_ted = pg.PlotWidget(self)
        # 设置该控件尺寸和相对位置
        self.plotWidget_ted.setGeometry(QtCore.QRect(20,20,400,300))

        # 仿写 mode1 代码中的数据
        # 生成 300 个正态分布的随机数
        title = options['title']
        # self.plotWidget_ted.setYRange(-1,1)
        self.plotWidget_ted.setLabel("left","value",units='V')
        self.plotWidget_ted.setTitle(title)
        self.plotWidget_ted.setBackground((255, 255, 255))
        # self.plotWidget_ted.setConfigOption('WheelSpin', False)
        # self.plotWidget_ted.
        self.curve1 = self.plotWidget_ted.plot(options['data'], name="mode1")

