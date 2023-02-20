
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
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtUiTools import QUiLoader
import time
# import utils.backend_server_sim as backend 
import pages.incomeQthread as Qthread

import pages.userTable as ut
import utils.gol as gol
import cv2
# 主页面信号
class mainSignal(QObject):
    setMainPage= Signal(int)
main_signal = mainSignal()

class income(QWidget):
    MainSignal= Signal()
    def __init__(self, ui, arg=None):
        super(income, self).__init__(arg)
        self.ui = ui
        # 实例化需要多线程直接方法的类，里面包含执行方法
        self.work = Qthread.Worker()
        # 实例化QThread，开启一个新线程对象
        self.work_thread = QThread()
        # 将执行方法的类的线程指向转移至新的线程对象
        self.work.moveToThread(self.work_thread)
        self.MainSignal.connect(self.work.connectServer)
        self.work.getPicSignal.connect(self.getPic)

        self.work_thread.start()
        self.MainSignal.emit()

        # 场景
        self.scene = QGraphicsScene()  # 创建画布
        self.ui.graphicsView.setScene(self.scene)  # 把画布添加到窗口
        self.scene2 = QGraphicsScene()  # 创建画布
        self.ui.graphicsView_2.setScene(self.scene2)  # 把画布添加到窗口
        
        self.scene3 = QGraphicsScene()  # 创建画布
        self.ui.graphicsView_3.setScene(self.scene3)  # 把画布添加到窗口
        # self.work.connectServer()
    def getPic(self,img):
        # print('img')
        print('getImg',str(time.time()))
        cutimg = img[0:1080,0:1440]
        cutimg2 = img[0:1080,1440:2880]
        cvimg = cv2.resize(cutimg, (480,270))
        frame = QImage(cvimg, 480, 270, QImage.Format_RGB888)
        cvimg2 = cv2.resize(cutimg2, (480,270))
        frame2 = QImage(cvimg2, 480, 270, QImage.Format_RGB888)
        # self.scene.clear()  #先清空上次的残留
        self.pix = QPixmap.fromImage(frame)
        self.scene.addPixmap(self.pix)

        self.pix2 = QPixmap.fromImage(frame2)
        self.scene2.addPixmap(self.pix2)
        self.scene3.addPixmap(self.pix2)
        # img = cv2.imdecode(data, cv2.IMREAD_COLOR)
        # cv2.imshow("part", img)
        # cv2.waitKey(1)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # showImage = QImage(img.data, img.shape[1], img.shape[0], img.shape[1] * 3,QImage.Forma
        # pix_img = QPixmap.fromImage(showImage).scaled(300, 180, Qt.KeepAspectRatio)
        # self.ui.label_video_camera.setPixmap(pix_img)
    def connectServer(self):
        self.work.connectSignal.emit()
    def close_event(self, event):
        print('exit!!!!!!')
