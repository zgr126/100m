
import numpy as np

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import QTimer, QThread, Signal, Slot
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtUiTools import QUiLoader
import utils.QFlowLayout as uQ
import time

import pages.userDetails as ud
import utils.db as db
import calc.main2 as cm
import pyqtgraph as pg

# 主页面信号
class mainSignal(QObject):
    setMainPage= Signal(int)
main_signal = mainSignal()

class Page(QWidget):
    data = []
    def __init__(self, data,arg=None):
        super(Page, self).__init__(arg)
        self.data = data
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        l = QLabel('百米基础属性')
        self.layout.addWidget(l)
        List9 = cm.List9(self.data)

        self.table = QTableWidget(2, 8)  # 3 行 5 列的表格
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自适应宽度
        self.table.setMaximumHeight(120)
        self.table.setHorizontalHeaderLabels(['项目', '速度', '躯干俯仰角', '平均绝对步长', '平均相对步长', '步频', '重心水平位移', '重心垂直位移'])
        self.layout.addWidget(self.table)
        self.table.setItem(0,0,QTableWidgetItem('当前项目'))

        l2 = QLabel('每10米分段时间')
        self.layout.addWidget(l2)

        self.table2 = QTableWidget(2, 11)  # 3 行 5 列的表格
        self.table2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自适应宽度
        self.table2.setMaximumHeight(120)
        self.table2.setHorizontalHeaderLabels(['项目', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'])
        self.table2.setItem(0,0,QTableWidgetItem('当前项目'))
        
        self.layout.addWidget(self.table2)

        # List9 = cm.List9(self.data)
        # option1 = {'data':[List9['PerSpeed']],
        #     'title':'水平面投影角加速度',
        #     'yAxis':['加速度','rad/s²']}
        # # self.layout.addStretch()
        self.setTable(List9,0)
        
    def setTable(self, List9,userIndex):
        print(List9)
        # table1
        self.table.setItem(userIndex,1,QTableWidgetItem(str(round(List9['AvgSpeed'],2))))
        self.table.setItem(userIndex,2,QTableWidgetItem(str(round(List9['AvgAngleNormal'],2))))
        self.table.setItem(userIndex,3,QTableWidgetItem(str(round(List9['StepSize'],2))))
        self.table.setItem(userIndex,4,QTableWidgetItem(str(round(List9['StepSize_height'],2))))
        self.table.setItem(userIndex,5,QTableWidgetItem(str(round(List9['StepNum'],2))))
        self.table.setItem(userIndex,6,QTableWidgetItem(str(round(List9['AvgVertCenter'],2))))
        self.table.setItem(userIndex,7,QTableWidgetItem(str(round(List9['AvgLevelCenter'],2))))
        # table2
        for index, pitem in enumerate(List9['PerTime']):
            self.table2.setItem(userIndex,index+1,QTableWidgetItem(str(round(pitem,2))))
        # picList
        a = self.layout.findChild(QScrollArea, 'formArea')
        if a != None:
            self.layout.removeWidget(a)

        option1 = [{'data':List9['PerSpeed'],
            'xData': ['项目', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'],
            'title':'运动员在每10米分段平均速度',
            'yAxis':['速度','m/s']}]
        self.formWid = setPage(option1)
        self.layout.addWidget(self.formWid)
        # self.layout.wid
def formScrollArea(options):
    listW = setPage(options)
    # 展示区域
    qscrollarea = QtWidgets.QScrollArea()
    qscrollarea.setContentsMargins(0,0,0,0)
    qscrollarea.setGeometry(QRect(50,100,600,500))
    qscrollarea.setWidgetResizable(True)
    qscrollarea.setWidget(listW)
    # layout.addWidget(qscrollarea)
    qscrollarea.setObjectName('formArea')
    return qscrollarea
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
    return listW
class Window(QWidget):
    def __init__(self, options):
        super().__init__()
        # 设置下尺寸
        self.resize(400,300)
        # 添加 PlotWidget 控件
        self.plotWidget_ted = pg.PlotWidget(self)
        # 设置该控件尺寸和相对位置
        self.plotWidget_ted.setGeometry(QtCore.QRect(0,0,400,300))
        self.setFixedWidth(400)
        self.setFixedHeight(300)
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
        hasX = options['xData'] is not None
        if hasX:
            xdict = dict(enumerate(options['xData'][1:]))
            x = list(xdict.values())
            ticks = [(i, j) for i, j in zip(range(10), options['xData'][1:])]
            print(ticks)
            self.curve1 = self.plotWidget_ted.plot(options['data'][:10], name="mode1")
            xax = self.plotWidget_ted.getAxis('bottom')
            xax.setTicks([ticks])
        else:
            self.curve1 = self.plotWidget_ted.plot(options['data'], name="mode1")
        
        
