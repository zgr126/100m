# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1018, 812)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMaximumSize(QSize(150, 16777215))
        self.widget_2.setStyleSheet(u"width:500;")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.p1 = QPushButton(self.widget_2)
        self.p1.setObjectName(u"p1")

        self.verticalLayout.addWidget(self.p1)

        self.p2 = QPushButton(self.widget_2)
        self.p2.setObjectName(u"p2")

        self.verticalLayout.addWidget(self.p2)

        self.p3 = QPushButton(self.widget_2)
        self.p3.setObjectName(u"p3")

        self.verticalLayout.addWidget(self.p3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.container = QStackedWidget(self.widget_3)
        self.container.setObjectName(u"container")
        self.income = QWidget()
        self.income.setObjectName(u"income")
        self.verticalLayout_4 = QVBoxLayout(self.income)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.time = QWidget(self.income)
        self.time.setObjectName(u"time")
        self.time.setMaximumSize(QSize(16777215, 1))
        self.horizontalLayout_6 = QHBoxLayout(self.time)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.time)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.label_7 = QLabel(self.time)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.time)

        self.pannel = QWidget(self.income)
        self.pannel.setObjectName(u"pannel")
        self.pannel.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(self.pannel)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.pannel)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(80, 16777215))
        self.label_3.setStyleSheet(u"width:50\n"
"")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.pannel)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.label_4)

        self.changeModeBtn = QPushButton(self.pannel)
        self.changeModeBtn.setObjectName(u"changeModeBtn")
        self.changeModeBtn.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.changeModeBtn)

        self.widget_6 = QWidget(self.pannel)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(146, 0))

        self.horizontalLayout.addWidget(self.widget_6)

        self.recordBtn = QPushButton(self.pannel)
        self.recordBtn.setObjectName(u"recordBtn")
        self.recordBtn.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.recordBtn)

        self.recordLight = QLabel(self.pannel)
        self.recordLight.setObjectName(u"recordLight")
        self.recordLight.setMaximumSize(QSize(10, 16777215))
        self.recordLight.setStyleSheet(u"color:red")

        self.horizontalLayout.addWidget(self.recordLight)

        self.recordTime = QLabel(self.pannel)
        self.recordTime.setObjectName(u"recordTime")

        self.horizontalLayout.addWidget(self.recordTime)


        self.verticalLayout_4.addWidget(self.pannel)

        self.widget_4 = QWidget(self.income)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 350))
        self.gridLayout = QGridLayout(self.widget_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.graphicsView_2 = QGraphicsView(self.widget_4)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.gridLayout.addWidget(self.graphicsView_2, 0, 2, 2, 2)

        self.graphicsView = QGraphicsView(self.widget_4)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 1, 1, 1, 1)

        self.graphicsView_3 = QGraphicsView(self.widget_4)
        self.graphicsView_3.setObjectName(u"graphicsView_3")

        self.gridLayout.addWidget(self.graphicsView_3, 1, 4, 1, 1)


        self.verticalLayout_4.addWidget(self.widget_4)

        self.posbox = QWidget(self.income)
        self.posbox.setObjectName(u"posbox")
        self.horizontalLayout_8 = QHBoxLayout(self.posbox)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")

        self.verticalLayout_4.addWidget(self.posbox)

        self.container.addWidget(self.income)
        self.record = QWidget()
        self.record.setObjectName(u"record")
        self.container.addWidget(self.record)
        self.user = QWidget()
        self.user.setObjectName(u"user")
        self.verticalLayout_2 = QVBoxLayout(self.user)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget1 = QWidget(self.user)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setMaximumSize(QSize(500, 16777215))
        self.horizontalLayout_4 = QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.widget1)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.widget1)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.addUserBtn = QPushButton(self.widget1)
        self.addUserBtn.setObjectName(u"addUserBtn")

        self.horizontalLayout_4.addWidget(self.addUserBtn)


        self.verticalLayout_2.addWidget(self.widget1)

        self.scrollArea = QScrollArea(self.user)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 869, 684))
        self.horizontalLayout_5 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_5.addWidget(self.tableWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.container.addWidget(self.user)
        self.recordDetail = QWidget()
        self.recordDetail.setObjectName(u"recordDetail")
        self.container.addWidget(self.recordDetail)

        self.horizontalLayout_3.addWidget(self.container)


        self.horizontalLayout_2.addWidget(self.widget_3)


        self.verticalLayout_3.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1018, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.container.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u767e\u7c73\u6280\u672f\u6d4b\u8bc4", None))
        self.p1.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u91c7\u96c6", None))
        self.p2.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u52a8\u5458\u540d\u5355", None))
        self.p3.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u67e5\u770b\u4e0e\u5bf9\u6bd4", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"2023\u5e7412\u670810\u65e5  12:30:30", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u5f55\u5236\u72b6\u6001\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8", None))
        self.changeModeBtn.setText(QCoreApplication.translate("MainWindow", u"\u5207\u6362\u6210\u624b\u52a8", None))
        self.recordBtn.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5f55\u5236", None))
        self.recordLight.setText(QCoreApplication.translate("MainWindow", u"\u25cf", None))
        self.recordTime.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u52a8\u5458\u59d3\u540d\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.addUserBtn.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u8fd0\u52a8\u5458", None))
    # retranslateUi

