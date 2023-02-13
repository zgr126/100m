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

import matplotlib
matplotlib.use("Qt5Agg")


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

class FigureCanvasDemo3(FigureCanvas):
    def __init__(self, parent=None, width=10, height=5):
        fig = Figure(figsize=(width, height), tight_layout=True)
        FigureCanvas.__init__(self, fig)
        self.axes = fig.add_subplot()

        # 开始作图
        x = np.linspace(0, 10, 100)
        y = 2 * np.sin(2 * x)
        self.axes.plot(x, y)
        self.axes.set_title('样例-sin图像')

        self.axes.grid()
        self.draw()
