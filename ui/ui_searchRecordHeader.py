# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchRecordHeader.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_searchBar(object):
    def setupUi(self, searchBar):
        if not searchBar.objectName():
            searchBar.setObjectName(u"searchBar")
        searchBar.resize(680, 27)
        self.horizontalLayout_2 = QHBoxLayout(searchBar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(searchBar)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(searchBar)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(140, 0))
        self.lineEdit.setStyleSheet(u"margin-right:10")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(searchBar)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.startDateTime = QDateTimeEdit(searchBar)
        self.startDateTime.setObjectName(u"startDateTime")

        self.horizontalLayout.addWidget(self.startDateTime)

        self.label_3 = QLabel(searchBar)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.endDateTime = QDateTimeEdit(searchBar)
        self.endDateTime.setObjectName(u"endDateTime")
        self.endDateTime.setStyleSheet(u"margin-right:10")

        self.horizontalLayout.addWidget(self.endDateTime)

        self.pushButton = QPushButton(searchBar)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn = QPushButton(searchBar)
        self.btn.setObjectName(u"btn")

        self.horizontalLayout.addWidget(self.btn)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(searchBar)

        QMetaObject.connectSlotsByName(searchBar)
    # setupUi

    def retranslateUi(self, searchBar):
        searchBar.setWindowTitle(QCoreApplication.translate("searchBar", u"Form", None))
        self.label.setText(QCoreApplication.translate("searchBar", u"\u8fd0\u52a8\u5458\u59d3\u540d\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("searchBar", u"\u8d77\u6b62\u65e5\u671f\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("searchBar", u"-", None))
        self.pushButton.setText(QCoreApplication.translate("searchBar", u"\u641c\u7d22", None))
        self.btn.setText(QCoreApplication.translate("searchBar", u"\u6dfb\u52a0", None))
    # retranslateUi

