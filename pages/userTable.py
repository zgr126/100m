
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

import pages.userDetails as ud
import utils.db as db

# 主页面信号
class mainSignal(QObject):
    setMainPage= Signal(int)
main_signal = mainSignal()

class TableView(QWidget):
    data = []
    def __init__(self, ui,arg=None):
        
        super(TableView, self).__init__(arg)
        self.ui = ui

        self.tableWidget = self.ui.tableWidget
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(['运动员姓名', '教练姓名', '年龄', '身高', '体重', '操作'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        


        # self.ui.tableWidget = self.tableWidget
        # 添加数据
        # item11 = QStandardItem('10')
        # item12 = QStandardItem('雷神')
        # item13 = QStandardItem('2000')
        # item14 = QStandardItem()
        # self.model.appendRow([item11,item12,item13, item14])
        # button = QToolButton()
        # self.tableWidget.(item14.index(), button)

        # item31 = QStandardItem('30')
        # item32 = QStandardItem('死亡女神')
        # item33 = QStandardItem('3000')
        # self.model.setItem(2, 0, item31)
        # self.model.setItem(2, 1, item32)
        # self.model.setItem(2, 2, item33)

        # layout = QVBoxLayout()
        # layout.addWidget(self.tableWidget)
        # self.setLayout(layout)
        # ui.tableWidget.setModel(self.model)
        ui.addUserBtn.clicked.connect(self.addUser)
        self.refrushUserPage('')
        
        
    def addUser(self):
        # self.ui = QUiLoader().load('./ui/user.ui')
        
        # layout = QBoxLayout()
        # dialog.setLayout(layout)
        # layout.addWidget(self.ui)
        self.ud = ud.userDetails(None)
        self.ud.userDetailsSignal.connect(self.addUserClick)
        self.ud.show()
    def addUserClick(self,int):
        self.ud.close()
        self.refrushUserPage('')
    def modifyUser(self, user):
        self.ud = ud.userDetails(user)
        self.ud.userDetailsSignal.connect(self.addUserClick)
        self.ud.show()
        pass
    def deleteUserCheck(self, user):
        box = QMessageBox(QMessageBox.Question, "提示", '是否确认删除运动员"{}"'.format(user[0]), QMessageBox.NoButton, self)
        yr_btn = box.addButton(self.tr("是"), QMessageBox.YesRole)
        box.addButton(self.tr("否"), QMessageBox.NoRole)
        box.exec_()
        if box.clickedButton() == yr_btn:
            self.deleteUser(user)
            return
        else:
            box.close()
            print('cancel')
    def deleteUser(self, user):
        c = db.db.cursor()
        sql = "DELETE FROM USER WHERE ID = {}".format(user[5])
        cursor = c.execute(sql)
        c.close()
        db.db.commit()
        self.refrushUserPage('')
    def refrushUserPage(self, username):
        c = db.db.cursor()
        sql = "SELECT name, age, height, weight, trainer, id FROM USER"
        if (username != ''):
            sql += " WHRER name = {}".format(username)
        cursor = c.execute(sql)
        data = c.fetchall()
        self.data = data
        self.makeFrom()
        c.close()
        db.db.commit()
    def makeFrom(self):
        l = len(self.data)
        self.tableWidget.setRowCount(l)
        s = QTableWidget
        def t2(value):
            return lambda: self.deleteUserCheck(value)
        def t(value):
            return lambda: self.modifyUser(value)
        for i, v in enumerate(self.data):
            s1 = QTableWidgetItem(v[0])
            self.tableWidget.setItem(i,0,s1)
            s2 = QTableWidgetItem(str(v[1]))
            self.tableWidget.setItem(i,2,s2)
            s3 = QTableWidgetItem(str(v[2]))
            
            self.tableWidget.setItem(i,3,s3)
            s4 = QTableWidgetItem(str(v[3]))
            self.tableWidget.setItem(i,4,s4)
            s5 = QTableWidgetItem(str(v[4]))
            self.tableWidget.setItem(i,1,s5)
            btnBox = QWidget()
            btnBoxLayout = QHBoxLayout(btnBox)
            btn = QPushButton('修改')
            btn2 = QPushButton('删除')
            btnBoxLayout.setContentsMargins(0,0,0,0)
            btnBoxLayout.addWidget(btn)
            btnBoxLayout.addWidget(btn2)
            btn2.clicked.connect(t2(v))
            btn.clicked.connect(t(v))
            self.tableWidget.setCellWidget(i,5, btnBox)
        
    def searchUser():
        pass
    def close_event(self, event):
        print('exit!!!!!!')