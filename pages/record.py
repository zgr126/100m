
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
import utils.db as db

import pages.userTable as ut
import random
# 主页面信号
class mainSignal(QObject):
    setMainPage= Signal(int)
main_signal = mainSignal()

class user(QWidget):
    def __init__(self, ui, arg=None):
        super(user, self).__init__(arg)
        self.ui = ui
        self.table = ut.TableView(ui)
    def close_event(self, event):
        print('exit!!!!!!')


class TableWidget(QWidget):
    control_signal = Signal(list)
    select_signal = Signal(list)
    data = []
    allDataLen = 0
    currentPage = 1
    def __init__(self, *args, **kwargs):
        super(TableWidget, self).__init__(*args, **kwargs)
        self.__init_ui()
        self.refrushPage()
    def __init_ui(self):
        style_sheet = """
            QTableWidget {
                border: none;
                background-color:rgb(240,240,240)
            }
            QPushButton{
                max-width: 18ex;
                max-height: 6ex;
                font-size: 11px;
            }
            QLineEdit{
                max-width: 30px
            }
        """
        self.table = QTableWidget(3, 4)  # 3 行 5 列的表格
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自适应宽度
        self.table.setHorizontalHeaderLabels(['运动员姓名', '日期', '成绩', '操作'])
        self.__layout = QVBoxLayout()
        # 搜索框
        self.header = QUiLoader().load('./ui/searchRecordHeader.ui')
        self.header.pushButton.clicked.connect(self.search)
        self.header.endDateTime.setDateTime(QDateTime.currentDateTime().addDays(30))
        self.header.btn.clicked.connect(self.insertRecord)

        self.__layout.addWidget(self.header)
        self.__layout.addWidget(self.table)
        
        self.setLayout(self.__layout)
        self.setStyleSheet(style_sheet)
    def search(self):
        st = self.header.startDateTime.dateTime().toPython()
        et = self.header.endDateTime.dateTime().toPython()
        
        self.currentPage = 1
        self.refrushPage()
        self.control_signal.emit(["home", self.currentPage])
    def setPageController(self, page):
        """自定义页码控制器"""
        control_layout = QHBoxLayout()
        homePage = QPushButton("首页")
        prePage = QPushButton("<上一页")
        self.curPage = QLabel("1")
        nextPage = QPushButton("下一页>")
        finalPage = QPushButton("尾页")
        self.totalPage = QLabel("共" + str(page) + "页")
        skipLable_0 = QLabel("跳到")
        self.skipPage = QLineEdit()
        skipLabel_1 = QLabel("页")
        confirmSkip = QPushButton("确定")
        homePage.clicked.connect(self.__home_page)
        prePage.clicked.connect(self.__pre_page)
        nextPage.clicked.connect(self.__next_page)
        finalPage.clicked.connect(self.__final_page)
        confirmSkip.clicked.connect(self.__confirm_skip)
        control_layout.addStretch(1)
        control_layout.addWidget(homePage)
        control_layout.addWidget(prePage)
        control_layout.addWidget(self.curPage)
        control_layout.addWidget(nextPage)
        control_layout.addWidget(finalPage)
        control_layout.addWidget(self.totalPage)
        control_layout.addWidget(skipLable_0)
        control_layout.addWidget(self.skipPage)
        control_layout.addWidget(skipLabel_1)
        control_layout.addWidget(confirmSkip)
        control_layout.addStretch(1)
        self.__layout.addLayout(control_layout)

    def __home_page(self):
        """点击首页信号"""
        self.control_signal.emit(["home", self.currentPage])

    def __pre_page(self):
        """点击上一页信号"""
        self.control_signal.emit(["pre", self.currentPage])

    def __next_page(self):
        """点击下一页信号"""
        self.control_signal.emit(["next", self.currentPage])

    def __final_page(self):
        """尾页点击信号"""
        self.control_signal.emit(["final", self.currentPage])

    def __confirm_skip(self):
        """跳转页码确定"""
        self.control_signal.emit(["confirm", self.skipPage.text()])

    def showTotalPage(self):
        """返回当前总页数"""
        return self.allDataLen//10+1
    def refrushPage(self):
        c = db.db.cursor()
        sql = "SELECT COUNT(*) FROM RECORD WHERE name LIKE '%{}%' AND startTime >= '{}' AND endTime <= '{}'".format(self.header.lineEdit.text(), self.header.startDateTime.dateTime().toPython(), self.header.endDateTime.dateTime().toPython()) 
        v = c.execute(sql)
        self.allDataLen = v.fetchone()[0]
        sql = "SELECT name, projectName, startTime, endTime, useTime, remark, id FROM RECORD WHERE name LIKE '%{}%' AND startTime >= '{}' AND endTime <= '{}' LIMIT 10 OFFSET {}".format(self.header.lineEdit.text(), self.header.startDateTime.dateTime().toPython(), self.header.endDateTime.dateTime().toPython(), (self.currentPage-1)*10)
        # print(sql)
        cursor = c.execute(sql)
        self.data = c.fetchall()
        # print(self.data)
        c.close()
        self.makeFrom()
        db.db.commit()
    def makeFrom(self):
        self.tableWidget = self.table
        l = len(self.data)
        self.tableWidget.setRowCount(l)
        s = QTableWidget
        def t2(value):
            return lambda: self.deleteUserCheck(value)
        def t(value):
            return lambda: self.showUser(value)
        for i, v in enumerate(self.data):
            s1 = QTableWidgetItem(v[0])
            self.tableWidget.setItem(i,0,s1)
            s2 = QTableWidgetItem(str(v[2]))
            self.tableWidget.setItem(i,1,s2)
            s3 = QTableWidgetItem(str(v[4]))
            self.tableWidget.setItem(i,2,s3)
            btnBox = QWidget()
            btnBoxLayout = QHBoxLayout(btnBox)
            btn = QPushButton('查看')
            btn2 = QPushButton('删除')
            btnBoxLayout.setContentsMargins(0,0,0,0)
            btnBoxLayout.addWidget(btn)
            btnBoxLayout.addWidget(btn2)
            btn2.clicked.connect(t2(v))
            btn.clicked.connect(t(v))
            self.tableWidget.setCellWidget(i,3, btnBox)
    def showUser(self, record):
        self.select_signal.emit(record)
    def deleteUserCheck(self, user):
        box = QMessageBox(QMessageBox.Question, "提示", '是否确认删除该条记录"{}"'.format(user[0]), QMessageBox.NoButton, self)
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
        sql = "DELETE FROM RECORD WHERE ID = {}".format(user[5])
        cursor = c.execute(sql)
        c.close()
        db.db.commit()
        self.refrushPage()    
    def insertRecord(self):
        c = db.db.cursor()
        t = time.strftime("%Y-%m-%d %H:%M:%S")
        sql = "INSERT INTO RECORD (name,startTime,endTime,createTime,useTime,fps, remark) \
                VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.randomName(),t,t,t, '12.03', '30', self.randomName())
        cursor = c.execute(sql)
        # data = c.fetchall()
        c.close()
        db.db.commit()
    def randomName(self):
        first_name = ["王", "李", "张", "刘", "赵", "蒋", "孟", "陈", "徐", "杨", "沈", "马", "高", "殷", "上官", "钟", "常"]
        second_name = ["伟", "华", "建国", "洋", "刚", "万里", "爱民", "牧", "陆", "路", "昕", "鑫", "兵", "硕", "志宏", "峰", "磊", "雷", "文","明浩", "光", "超", "军", "达"]
        name = random.choice(first_name) + random.choice(second_name)
        return name
class MainWindow(QWidget):
    view_signal = Signal(list)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__init_ui()

    def __init_ui(self):
        self.resize(500, 250)
        self.setWindowTitle("QTableWidget加页码控制器")
        self.table_widget = TableWidget()  # 实例化表格
        self.table_widget.setPageController(10)  # 表格设置页码控制
        self.table_widget.control_signal.connect(self.page_controller)
        # self.setCentralWidget(self.table_widget)
        b = QVBoxLayout()
        self.setLayout(b)
        b.addWidget(self.table_widget) 
        self.table_widget.select_signal.connect(self.relay)
    def relay(self, lst):
        self.view_signal.emit(lst)
    def page_controller(self, signal):
        total_page = self.table_widget.showTotalPage()
        i = 1
        if "home" == signal[0]:
            i = 1
        elif "pre" == signal[0]:
            if 1 == int(signal[1]):
                QMessageBox.information(self, "提示", "已经是第一页了", QMessageBox.Yes)
                return
            i = int(signal[1]) - 1
        elif "next" == signal[0]:
            if total_page == int(signal[1]):
                QMessageBox.information(self, "提示", "已经是最后一页了", QMessageBox.Yes)
                return
            i = int(signal[1]) + 1
        elif "final" == signal[0]:
            i = total_page
        elif "confirm" == signal[0]:
            if total_page < int(signal[1]) or int(signal[1]) < 0:
                QMessageBox.information(self, "提示", "跳转页码超出范围", QMessageBox.Yes)
                return
            i = signal[1]
        self.table_widget.currentPage = i
        self.table_widget.curPage.setText(str(i))
        self.changeTableContent()  # 改变表格内容

    def changeTableContent(self):
        """根据当前页改变表格的内容"""
        self.table_widget.refrushPage()
        cur_page = self.table_widget.curPage.text()
        pass




# class FigureCanvasDemo3(FigureCanvas):
#     def __init__(self, parent=None, width=10, height=5):
#         fig = Figure(figsize=(width, height), tight_layout=True)
#         FigureCanvas.__init__(self, fig)
#         self.axes = fig.add_subplot()

#         # 开始作图
#         x = np.linspace(0, 10, 100)
#         y = 2 * np.sin(2 * x)
#         self.axes.plot(x, y)
#         self.axes.set_title('样例-sin图像')

#         self.axes.grid()
#         self.draw()
