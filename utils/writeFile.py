'''
Author: zgr126 zgr126@126.com
Date: 2023-01-10 14:52:55
LastEditors: zgr126 zgr126@126.com
LastEditTime: 2023-01-17 14:08:12
FilePath: \subingtianpy\main2.py
Description: 

Copyright (c) 2023 by zgr126 zgr126@126.com, All Rights Reserved. 
'''
import sys
import cv2
import time
import numpy as np
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer, QThread, Signal, Slot
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtUiTools import QUiLoader
#https://ru.stackoverflow.com/a/1150993/396441

class Thread1(QThread):
    changePixmap = Signal(QImage)
    
    def __init__(self, *args, **kwargs):
        super().__init__()

    def run(self):
        self.cap1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap1.set(3,1080)
        self.cap1.set(4,1920)
        self.cap1.set(5,30)
        while True:
            ret1, image1 = self.cap1.read()
            if ret1:
                im1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
                height1, width1, channel1 = im1.shape
                step1 = channel1 * width1
                qImg1 = QImage(im1.data, width1, height1, step1, QImage.Format_RGB888)
                self.changePixmap.emit(qImg1)

class Thread2(QThread):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.active = True

    def run(self):
        if self.active:            
            self.fourcc = cv2.VideoWriter_fourcc(*'XVID') 
            self.out1 = cv2.VideoWriter('output.avi', self.fourcc, 30, (1920,1080))
            self.cap1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            # self.cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
            # self.cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
            # self.cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
            # self.cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
            self.cap1.set(5, 30)
            while self.active:                      
                ret1, image1 = self.cap1.read()
                print(time.time())
                # print(image1)
                if ret1:
                    # self.out1.write(image1)   
                    wide_img = np.zeros((1080,1920, 3), np.uint8)  
                    self.out1.write(np.random.randint( 255, size=wide_img.shape, dtype=np.uint8 ))
                self.msleep(10)                      

    def stop(self):
        self.out1.release()

       
class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.resize(1940, 1100)
        self.control_bt = QPushButton('START')
        self.control_bt.clicked.connect(self.controlTimer)
        self.image_label = QLabel()
        self.saveTimer = QTimer()
        self.th1 = Thread1(self)
        self.th1.changePixmap.connect(self.setImage)
        self.th1.start()
        
        self.ui = QUiLoader().load('./m.ui')
        vlayout = QVBoxLayout(self)
        vlayout.addWidget(self.image_label)
        vlayout.addWidget(self.control_bt)   

    @QtCore.Slot(QImage)
    def setImage(self, qImg1):
        self.image_label.setPixmap(QPixmap.fromImage(qImg1))

    def controlTimer(self):
        if not self.saveTimer.isActive():
            # write video
            self.saveTimer.start()
            self.th2 = Thread2(self)
            self.th2.active = True                                
            self.th2.start()
            # update control_bt text
            self.control_bt.setText("STOP")
        else:
            # stop writing
            self.saveTimer.stop()
            self.th2.active = False                   
            self.th2.stop()                         
            self.th2.terminate()                    
            # update control_bt text
            self.control_bt.setText("START")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())