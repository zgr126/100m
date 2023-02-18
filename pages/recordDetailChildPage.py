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
    currentPageIndex = 0
    p4 = ['左肩','右肩','左肘','右肘','左腕','右腕',
    '左髋','右髋','左膝','右膝','左踝','右踝','重心']
    p5 = ['左肩','右肩','左肘','右肘',
    '左髋','右髋','左膝','右膝','双腿']
    p6 = ['左肩','右肩','左肘','右肘',
    '左髋','右髋','左膝','右膝','双腿']
    p7 = ['左肩','右肩','左肘','右肘',
    '左髋','右髋','左膝','右膝']
    p8 = ['左大臂','右大臂','左小臂','右小臂',
    '左大腿','右大腿','左小腿','右小腿','左躯干','右躯干']
    def __init__(self, page, data, arg=None):
        super(Page, self).__init__(arg)
        self.data = data
        
        self.pageIndex = page
        if page == 4:
            self.pageConifg = self.p4
        if page == 5:
            self.pageConifg = self.p5
        if page == 6:
            self.pageConifg = self.p6
        if page == 7:
            self.pageConifg = self.p7
        if page == 8:
            self.pageConifg = self.p8

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.addBtns(self.pageConifg))
        self.addWidget(0)
    def addWidget(self, ind):
        
        if self.pageIndex == 4:
            self.page = self.page4(ind)
        if self.pageIndex == 5:
            self.page = self.page5(ind)
        if self.pageIndex == 6:
            self.page = self.page6(ind)
        if self.pageIndex == 7:
            self.page = self.page7(ind)
        if self.pageIndex == 8:
            self.page = self.page8(ind)
        self.layout.addWidget(self.page)
        # if page == 9:
        #     self.layout.addWidget(self.page9())
        #     self.layout.addWidget(self.changePage(4))
        # btnGroup = self.changePage()
    def addBtns(self, p):
        btnW = QWidget()
        
        btnLay = QHBoxLayout()
        btnW.setLayout(btnLay)
        btg2=QButtonGroup(btnW)#创建一个按钮组
        def t(val):
            return lambda:self.changeId(val)
        for index, pitem in enumerate(p):
            rbt = QRadioButton(pitem)
            btnLay.addWidget(rbt)
            rbt.clicked.connect(t(index))
            # rbt.move(0,0)
            if index ==0:
                rbt.setChecked(True)
        btnLay.addStretch()
        return btnW
    def changeId(self,val):
        # 清除报表
        self.page.setParent(None)
        self.layout.removeWidget(self.page)
        print(val)
        self.addWidget(val)
        # rbt4 = QRadioButton("选项3",window)
        # rbt4.move(100, 0)
        # rbt5 = QRadioButton("选项4",window)
        # rbt5.move(100, 20)
        # rbt6 = QRadioButton("选项5",window)
        # rbt6.move(100, 40)
        # btg2=QButtonGroup()#创建一个按钮组
        # btg2.addButton(rbt4,3)#将单选按钮添加到按钮组，组成单选组。
        # btg2.addButton(rbt5,4)
        # btg2.addButton(rbt6,5)
        # btg2.buttonClicked.connect(butClicked)#添加事件
    def page4(self,ind):
        return setPage(cm.Show4(ind,self.data))
    def page5(self,ind):
        return setPage(cm.Show5(ind,self.data))
    def page6(self,ind):
        return setPage(cm.Show6(ind,self.data))
    def page7(self,ind):
        return setPage(cm.Show7(ind,self.data))
    def page8(self,ind):
        return setPage(cm.Show8(ind,self.data))
    # def page9(self):
    #     return setPage(cm.Show9(0,self.data))
def setPage(options):
    layout = uQ.FlowLayout()
    wid = QGroupBox()
    wid.setLayout(layout)
    # w= Window({'data':x1,
    #     'title': 'ind点xz面位移图(俯视)',
    #     'yAxix': ['z axis','帧率']
    #     })
    for i in options:
        w = Window(i)
        layout.addWidget(w)
    
    container_layout = QVBoxLayout()
    container_layout.setContentsMargins(0,0,0,0)
    listW = QListWidget()
    listW.setContentsMargins(0,0,0,0)
    listW.setLayout(container_layout)
    wid.setContentsMargins(0,0,0,0)
    container_layout.addWidget(wid)
    # container_layout.addStretch()
    # l = QWidget()
    qscrollarea = QtWidgets.QScrollArea()
    qscrollarea.setContentsMargins(0,0,0,0)
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
        self.setFixedWidth(440)
        self.setFixedHeight(340)
        self.setStyleSheet('''
            QWidget {
                margin: 0ex;
            }
            QWidget:enabled {
                border: 1px solid black;
            }
            QWidget::title {
                subcontrol-origin: margin;
                left: 1ex;
            }''')
        # 仿写 mode1 代码中的数据
        # 生成 300 个正态分布的随机数
        title = options['title']
        # self.plotWidget_ted.setYRange(-1,1)
        self.plotWidget_ted.setLabel("left",options['yAxis'][0],units=options['yAxis'][1])
        self.plotWidget_ted.setTitle(title)
        self.plotWidget_ted.setBackground((255, 255, 255))
        # self.plotWidget_ted.setConfigOption('WheelSpin', False)
        # self.plotWidget_ted.
        self.curve1 = self.plotWidget_ted.plot(options['data'], name="mode1")

