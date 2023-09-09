# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'mainui.ui'
##
# Created by: Qt User Interface Compiler version 6.5.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                               QMainWindow, QPushButton, QSizePolicy, QStatusBar,
                               QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(341, 416)
        MainWindow.setStyleSheet(u"QPushButton{\n"
                                 "	color:#ffffff; /*\u6587\u5b57\u989c\u8272*/\n"
                                 "	background-color:qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0, stop:0 #eeaeca, stop: 1 #94bbe9);/*\u80cc\u666f\u8272*/\n"
                                 "	border-style:outset; /*\u8fb9\u6846\u98ce\u683c*/\n"
                                 "	border-width:2px;/*\u8fb9\u6846\u5bbd\u5ea6*/\n"
                                 "	border-radius:10px; /*\u8fb9\u6846\u5012\u89d2*/\n"
                                 "	font:bold 14px; /*\u5b57\u4f53*/\n"
                                 " 	font-family: \"Microsoft YaHei\";\n"
                                 "	min-width:100px;/*\u63a7\u4ef6\u6700\u5c0f\u5bbd\u5ea6*/\n"
                                 "	min-height:25px;/*\u63a7\u4ef6\u6700\u5c0f\u9ad8\u5ea6*/\n"
                                 "	padding:4px;/*\u5185\u8fb9\u8ddd*/\n"
                                 "}\n"
                                 "QLabel {\n"
                                 "	color: #6f9aca;\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 271, 41))
        self.label.setStyleSheet(u"")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 50, 311, 71))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 132, 322, 256))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_8, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 3, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.widget)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout.addWidget(self.pushButton_10, 4, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.widget)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout.addWidget(self.pushButton_11, 4, 1, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.pushButton_9)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_7.clicked.connect(MainWindow.msg1)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"CMFW mini 1.85", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Clash Meta For Windows Mini</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u8fd0\u884c\u72b6\u6001\uff1a</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">NaN</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u5185\u5b58\u5360\u7528\uff1a</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">NaN</span></p></body></html>", None))
        self.pushButton_7.setText(QCoreApplication.translate(
            "MainWindow", u"Clash Meta \u670d\u52a1\u5b89\u88c5", None))
        self.pushButton_8.setText(QCoreApplication.translate(
            "MainWindow", u"Clash Meta \u670d\u52a1\u5b89\u88c5", None))
        self.pushButton.setText(QCoreApplication.translate(
            "MainWindow", u"Clash Meta \u670d\u52a1\u542f\u52a8", None))
        self.pushButton_2.setText(QCoreApplication.translate(
            "MainWindow", u"Clash Meta \u670d\u52a1\u505c\u6b62", None))
        self.pushButton_3.setText(QCoreApplication.translate(
            "MainWindow", u"Tun/\u7cfb\u7edf\u4ee3\u7406 \u6a21\u5f0f\u5207\u6362", None))
        self.pushButton_5.setText(QCoreApplication.translate(
            "MainWindow", u"\u66f4\u65b0 Alpha \u5185\u6838", None))
        self.pushButton_4.setText(QCoreApplication.translate(
            "MainWindow", u"\u66f4\u65b0yacd-meta", None))
        self.pushButton_6.setText(QCoreApplication.translate(
            "MainWindow", u"\u6253\u5f00 Yacd \u9762\u677f", None))
        self.pushButton_10.setText(QCoreApplication.translate(
            "MainWindow", u"\u4e0b\u8f7d\u914d\u7f6e\u6587\u4ef6", None))
        self.pushButton_11.setText(QCoreApplication.translate(
            "MainWindow", u"\u66f4\u65b0\u914d\u7f6e\u6587\u4ef6", None))
        self.pushButton_9.setText(QCoreApplication.translate(
            "MainWindow", u"\u9000\u51fa", None))
    # retranslateUi
