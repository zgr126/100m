import os
import sys
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import QTimer, QThread, Signal, Slot
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtUiTools import QUiLoader
 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 300)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pyqtgraph example"))
 
class MainWindow(QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet("background-color:rgb(255,255,255)")
        self.showLineChart()
        
    def showLineChart(self):
        # 创建一个GraphicsWidget
        win = pg.GraphicsLayoutWidget(self, show=True)
        # 设置widget大小
        win.resize(600, 300)
        # 创建一个Plot画板
        plot = win.addPlot(title="柱状图例子")
        # 加入随机的点数据
        barItem = pg.BarGraphItem(x=[1,2,3,4,5],height=[10,12,2,15,20,0], width = 0.5, brush=(107,200,224))
        plot.addItem(barItem)
        
 
if __name__ == '__main__':
    # 设置背景色
    pg.setConfigOption('background', 'w')
    # 设置平滑绘制
    pg.setConfigOptions(antialias = True)
    # 创建Application
    app = QApplication(sys.argv)
    # 创建对话框
    mainWidget = MainWindow()
    # 对话框显示
    mainWidget.show()
    # 执行app
    sys.exit(app.exec_())