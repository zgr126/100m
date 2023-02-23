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

import pages.recordDetailChildPage as pr

import pyqtgraph as pg

import calc.ReadData as cR
import pages.recordDetailData as rData
import pages.recordRely as rRely
from .record import MainWindow
import calc.main2 as cm

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
        self.ui.t4.clicked.connect(lambda: self.changePage(4))
        self.ui.t5.clicked.connect(lambda: self.changePage(5))
        self.ui.t6.clicked.connect(lambda: self.changePage(6))
        self.ui.t7.clicked.connect(lambda: self.changePage(7))
        self.ui.t8.clicked.connect(lambda: self.changePage(8))
        self.ui.t9.clicked.connect(lambda: self.changePage(9))
        self.ui.t10.clicked.connect(lambda: self.changePage(10))
        
        # self.detailsPage = self.ui.details #9  10 详情页
        self.layout2 =  QVBoxLayout()
        self.ui.details.setLayout(self.layout2)

        self.ui.stackedWidget.setCurrentIndex(0)
        self.changePage(9)
        self.ui.contrastBtn.clicked.connect(self.contrastDialog)
    def contrastDialog(self):
        win = MainWindow('查看')
        self.contrastWidget = win
        self.contrastWidget.show()
        self.contrastWidget.setWindowModality(Qt.ApplicationModal)
        self.contrastWidget.setFixedSize(800, 500)
        win.view_signal.connect(self.selectContrast)
        pass
    def selectContrast(self, l):
        self.ui.contrastLabel.setText('姓名：{}  时间：{}  项目说明：{}'.format(l[0],l[2],l[1]))
        self.contrastData = cm.List9(cR.ReadData())
        self.setContrastData()
        self.contrastWidget.close()
    def setContrastData(self):
        # self.childPageData = cR.ReadData()
        self.rData.setContrast(self.contrastData)
    def removePage(self):
        # 移除layout
        self.pr.setParent(None)
        self.layout.removeWidget(self.pr)
    def initPage(self,page):
        
        self.pr = pr.Page(page, self.childPageData)
        self.layout.addWidget(self.pr)
    def changePage(self, value):
        if value == 9 or value == 10:
            self.ui.stackedWidget.setCurrentIndex(1)
            # self.layout2 =  QVBoxLayout()
            # self.ui.details.setLayout(self.layout2)
            # self.table = QTableWidget(3, 4)  # 3 行 5 列的表格
            # self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自适应宽度
            # self.table.setHorizontalHeaderLabels(['运动员姓名', '日期', '成绩', '操作'])
            # self.layout2.addWidget(self.table)
            # self.ui.layout2.addWidget(self.table)
            # print(self.layout2.parent())
            # hasChild = len(self.layout2.children()) != 0
            # if hasChild:
            #     p = self.layout2.children()[0]
            #     p.setParent(None)
            #     self.detailsPage.removeWidget(p)
            self.layout2 =  QHBoxLayout()
            self.ui.details.setLayout(self.layout2)
            if value == 9:
                # self.detailsp = rData.Page(self.childPageData)
                # print(self.ui.details)
                # self.self.layout2.addWidget(self.detailsp)
                # print(self.self.layout2.children())
                # print(self.self.layout2.parentWidget())
                # self.rData = 
                # pr.Page(5, self.childPageData)#
                _rData = rData.Page(self.childPageData)
                self.layout2.addWidget(_rData)
                pass
            if value == 10:
                self.rRely = rRely.Page(self.childPageData)
                self.layout2.addWidget(rRely)
        else:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.removePage()
            self.initPage(value)
    def details(self, value):
        pass