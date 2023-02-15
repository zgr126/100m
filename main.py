
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
from PySide6.QtUiTools import QUiLoader
import time

import matplotlib
matplotlib.use("Qt5Agg")
import sqlite3

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号


import pages.user as user
import utils.db as db
import pages.record as record
import pages.recordDetail as recordD
# 主页面信号
class mainSignal(QObject):
    setMainPage= Signal(int)
main_signal = mainSignal()

# 主页面ui
class MainWindow(QMainWindow):
    currentPage = 0
    def __init__(self):
        super(MainWindow, self).__init__()
        # self.ui = Ui_MainWindow()
        self.ui = QUiLoader().load('./ui/main.ui')
        self.user = user.user(self.ui)
    # 记录详情页面
    def toDetail(self, record):
        print(record)
        self.leftClick(3)
        # 设置recordDetails
        b = QVBoxLayout()
        self.ui.recordDetail.setLayout(b)
        w = recordD.userDetails(record)
        b.addWidget(w.ui)
        # w.view_signal.connect(self.toDetail)
        # s.setCurrentIndex
    def show(self):
        self.ui.show()
        self.leftClick(1)
    def register(self):

        # v = changePage()
        self.ui.p1.clicked.connect(lambda:self.leftClick(0))
        self.ui.p2.clicked.connect(lambda:self.leftClick(2))
        self.ui.p3.clicked.connect(lambda:self.leftClick(1))
        # 显示图表
        # plot = FigureCanvasDemo3(
        #     width=self.ui.graphicsView.width() / 101,
        #     height=self.ui.graphicsView.height() / 101
        # )
        
        # graphicsScene = QGraphicsScene()  # 创建一个QGraphicsScene
        # graphicsScene.addWidget(plot)
        # self.ui.graphicsView.setScene(graphicsScene)
        # self.ui.graphicsView.show()  # 调用show方法呈现图形
    def leftClick(self, p):
        self.currentPage = p
        print(p)
        self.ui.container.setCurrentIndex(p)
        if p == 1:
            # 设置record
            b = QVBoxLayout()
            self.ui.record.setLayout(b)
            w = record.MainWindow()
            b.addWidget(w)
            w.view_signal.connect(self.toDetail)
       
    # def change
    def closeEvent(self, event):
        print('exit!!!!!!')
        sys.exit(0)

def exitfunc():
    db.db.close()
    print('exit')
sys.exitfunc = exitfunc

if __name__ == "__main__":
    # 所有应用必须创建一个应用（Application）对象
    # sys.argv参数是一个来自命令行的参数列表

    app = QApplication(sys.argv)
    window = MainWindow()
    window.register()
    window.show()
    # 应用进入主循环，事件处理开始执行。
    # 主循环用于接收来自窗口触发的事件，并且转发她们到widget应用上处理。
    # 如果调用exit()方法或主widget组件被销毁，主循环将退出。
    # sys.exit()方法确保一个不留垃圾的退出。系统环境将会被通知应用是怎么被结束的。
    sys.exit(app.exec())