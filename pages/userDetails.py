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


class userDetails(QDialog):
    userDetailsSignal = Signal(int)
    type = '新增'
    user = []
    def __init__(self, user, arg=None):
        super(userDetails, self).__init__(arg)
        # 判断user
        if user is None:
            self.type = '新增'
            
        else:
            self.type = '编辑'
            self.user = user
            self.ui.i1.setText(user[0])
            self.ui.i1.setText(user[1])
            self.ui.i1.setText(user[4])
            self.ui.i1.setText(user[2])
            self.ui.i1.setText(user[3])
        # s = QLabel()
        # s.setText
        self.ui = QUiLoader().load('./ui/user.ui')
        # flags = self.windowFlags()
        # self.ui.setWindowFlags(flags | Qt.WindowStaysOnTopHint)
        self.ui.setWindowModality(Qt.ApplicationModal)
        self.ui.setFixedSize(self.ui.width(), self.ui.height())
        self.ui.setWindowTitle('{}运动员'.format(self.type))
        self.ui.i2.setValidator(QtGui.QDoubleValidator())
        self.ui.i3.setValidator(QtGui.QDoubleValidator())
        self.ui.i5.setValidator(QtGui.QDoubleValidator())
        self.ui.pushButton.clicked.connect(self.click_btn)
    def show(self):
        self.ui.show()    
    def close_event(self, event):
        print('exit!!!!!!')
    def click_btn(self):
        t1= self.ui.i1.text()
        t2= self.ui.i2.text()
        t3= self.ui.i3.text()
        t4= self.ui.i4.text()
        t5= self.ui.i5.text()
        
        if ((t1 == '') | (t2 == '') | (t3 == '') | (t4 == '') | (t5 == '')):
            dialog = QMessageBox.information(self.ui, '信息', '请不要留空')
            dialog.show()
            return
        c = db.db.cursor()
        t = time.time()
        if self.type == '新增':
            sql = "INSERT INTO USER (name,age,weight,trainer,height, createTime) \
                VALUES ('{}', {}, {}, '{}', {}, {})".format(t1,t2,t3, t4, t5, t)
        else:
            sql = "UPDATE USER SET name = {}, age = {}, weight = {}, trainer = {}, height = {}, updateTime = {} \
                WHERE id = {}".format(t1,t2,t3,t4,t5,t,self.user[5])
        print(sql)
        cursor = c.execute(sql)
        
        c.close()
        db.db.commit()
        
        self.userDetailsSignal.emit(0)
        self.ui.close()