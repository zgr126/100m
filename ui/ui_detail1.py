# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detail1.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QScrollArea, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(924, 606)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 922, 604))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.f1 = QTableWidget(self.scrollAreaWidgetContents)
        if (self.f1.columnCount() < 8):
            self.f1.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.f1.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.f1.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.f1.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.f1.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.f1.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.f1.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.f1.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.f1.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.f1.rowCount() < 2):
            self.f1.setRowCount(2)
        self.f1.setObjectName(u"f1")
        self.f1.setMaximumSize(QSize(16777215, 120))
        self.f1.setRowCount(2)
        self.f1.setColumnCount(8)

        self.verticalLayout.addWidget(self.f1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.f2 = QTableWidget(self.scrollAreaWidgetContents)
        if (self.f2.columnCount() < 11):
            self.f2.setColumnCount(11)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.f2.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.f2.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.f2.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.f2.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.f2.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.f2.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.f2.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.f2.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.f2.setHorizontalHeaderItem(8, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.f2.setHorizontalHeaderItem(9, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.f2.setHorizontalHeaderItem(10, __qtablewidgetitem18)
        if (self.f2.rowCount() < 2):
            self.f2.setRowCount(2)
        self.f2.setObjectName(u"f2")
        self.f2.setMaximumSize(QSize(16777215, 120))
        self.f2.setRowCount(2)
        self.f2.setColumnCount(11)

        self.verticalLayout.addWidget(self.f2)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u767e\u7c73\u57fa\u7840\u5c5e\u6027", None))
        ___qtablewidgetitem = self.f1.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u9879\u76ee", None));
        ___qtablewidgetitem1 = self.f1.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u901f\u5ea6", None));
        ___qtablewidgetitem2 = self.f1.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u8eaf\u5e72\u4fef\u4ef0\u89d2", None));
        ___qtablewidgetitem3 = self.f1.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u5e73\u5747\u7edd\u5bf9\u6b65\u957f", None));
        ___qtablewidgetitem4 = self.f1.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u5e73\u5747\u76f8\u5bf9\u6b65\u957f", None));
        ___qtablewidgetitem5 = self.f1.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u6b65\u9891", None));
        ___qtablewidgetitem6 = self.f1.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"\u91cd\u5fc3\u6c34\u5e73\u4f4d\u79fb", None));
        ___qtablewidgetitem7 = self.f1.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"\u91cd\u5fc3\u5782\u76f4\u4f4d\u79fb", None));
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6bcf10\u7c73\u5206\u6bb5\u65f6\u95f4", None))
        ___qtablewidgetitem8 = self.f2.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"\u9879\u76ee", None));
        ___qtablewidgetitem9 = self.f2.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"10", None));
        ___qtablewidgetitem10 = self.f2.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"20", None));
        ___qtablewidgetitem11 = self.f2.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"30", None));
        ___qtablewidgetitem12 = self.f2.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"40", None));
        ___qtablewidgetitem13 = self.f2.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"50", None));
        ___qtablewidgetitem14 = self.f2.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"60", None));
        ___qtablewidgetitem15 = self.f2.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"70", None));
        ___qtablewidgetitem16 = self.f2.horizontalHeaderItem(8)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"80", None));
        ___qtablewidgetitem17 = self.f2.horizontalHeaderItem(9)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"90", None));
        ___qtablewidgetitem18 = self.f2.horizontalHeaderItem(10)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"100", None));
    # retranslateUi

