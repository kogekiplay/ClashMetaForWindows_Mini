# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import global_hotkeys as hotkey
from PySide6.QtCore import (QCoreApplication,QMetaObject,QRect,QTimer,QThread)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QStatusBar, QVBoxLayout, QWidget,QMessageBox)
from foo.test.tunmode import proxyswitch
from foo.test.service import startservice,stopservice,stopserviceonly,startserviceonly
from foo.test.update import updateyacd,updatecore,replacecore
from foo.test.yacdopen import yacdopen
from foo.test.checkapi import checkmemory

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(341, 361)
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
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 50, 311, 71))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 131, 320, 211))
        self.gridLayout = QGridLayout(self.widget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.widget1)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.widget1)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_8, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.widget1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.widget1)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.widget1)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.widget1)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.widget1)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.widget1)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 3, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.widget1)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_9, 4, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        # 创建一个定时器对象
        self.timer = QTimer()
        # 连接定时器的信号和更新标签的槽函数
        self.timer.timeout.connect(self.update_label)
        # 启动定时器，每隔5秒触发一次
        self.timer.start(5000)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_7.clicked.connect(self.installmsg)
        self.pushButton_8.clicked.connect(self.uninstallmsg)
        self.pushButton.clicked.connect(self.startservicemsg)
        self.pushButton_2.clicked.connect(self.stopservicemsg)
        self.pushButton_3.clicked.connect(self.proxyswitchmsg)
        self.pushButton_4.clicked.connect(self.updateyacdmsg)
        self.pushButton_5.clicked.connect(self.updatecoremsg)
        self.pushButton_6.clicked.connect(self.yacdopenmsg)
        self.pushButton_9.clicked.connect(self.quit)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CMFW mini 1.4", None))
        MainWindow.setWindowIcon(QIcon("img\logo.ico"))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Clash Meta For Windows Mini</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u8fd0\u884c\u72b6\u6001\uff1a</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">NaN</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u5185\u5b58\u5360\u7528\uff1a</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">NaN</span></p></body></html>", None))
        #启动的时候检查一次内存，并更新到上面
        self.update_label()
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Clash Meta 服务安装", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Clash Meta 服务卸载", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Clash Meta 服务启动", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Clash Meta 服务停止", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"tun/系统代理 模式切换", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"更新 alpha 内核", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"更新 Yacd-Meta", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"打开 yacd 面板", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"退出", None))
    # retranslateUi

    def update_label(self):
        # 调用获取内存信息的函数，返回一个字符串
        mem_info = checkmemory()
        # 设置标签的文本为内存信息字符串
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">{}</span></p></body></html>".format(mem_info), None))

    def installmsg(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("提示")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setWindowIcon(QIcon("img\logo.ico"))
        status = startservice()
        if status == True:
            msgBox.setIcon(QMessageBox.Icon.Information)
            msgBox.setText("服务安装并启动成功，自行检查log文件夹")
            msgBox.exec()
        elif status == False:
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setText("服务启动失败")
            msgBox.exec()
        elif status == "not exist":
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setText("\"config.yaml\"不存在")
            msgBox.exec()
        elif status == "no permission":
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setText("\"config.yaml\"无法写入")
            msgBox.exec()
        elif status == "error":
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setText("发生了意料之外的错误")
            msgBox.exec()
        else:
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setText(status)
            msgBox.exec()

    def uninstallmsg(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("提示")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setWindowIcon(QIcon("img\logo.ico"))
        status = stopservice()
        if status == True:
            msgBox.setIcon(QMessageBox.Icon.Information)
            msgBox.setText("服务卸载成功")
            msgBox.exec()
        elif status == False:
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setText("服务卸载失败（你安装成功了吗）")
            msgBox.exec()

    def startservicemsg(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("提示")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setWindowIcon(QIcon("img\logo.ico"))
        status=startserviceonly()
        if status == True:
            msgBox.setIcon(QMessageBox.Icon.Information)
            msgBox.setText("服务启动成功")
            msgBox.exec()
        elif status == False:
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setText("服务启动失败")
            msgBox.exec()
        elif status == "not exist":
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setText("\"config.yaml\"不存在")
            msgBox.exec()
        elif status == "no permission":
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setText("\"config.yaml\"无法写入")
            msgBox.exec()
        elif status == "error":
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setText("发生了意料之外的错误")
            msgBox.exec()
        else:
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setText(status)
            msgBox.exec()

    def stopservicemsg(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("提示")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setWindowIcon(QIcon("img\logo.ico"))
        status = stopserviceonly()
        if status == True:
            msgBox.setIcon(QMessageBox.Icon.Information)
            msgBox.setText("停止成功")
            msgBox.exec()
        elif status == False:
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setText("停止失败（你安装成功了吗）")
            msgBox.exec()

    
    def proxyswitchmsg(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("提示")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setWindowIcon(QIcon("img\logo.ico"))
        status = proxyswitch()
        if status == True:
            msgBox.setIcon(QMessageBox.Icon.Information)
            msgBox.setText("tun模式已开启,系统代理已关闭")
            msgBox.exec()
        elif status == False:
            msgBox.setIcon(QMessageBox.Icon.Information)
            msgBox.setText("tun模式已关闭,系统代理已开启")
            msgBox.exec()
    
    def updateyacdmsg(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("提示")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setWindowIcon(QIcon("img\logo.ico"))
        status = updateyacd()
        if status == True:
            msgBox.setIcon(QMessageBox.Icon.Information)
            msgBox.setText("更新成功")
            msgBox.exec()
        else:
            msgBox.setIcon(QMessageBox.Icon.Information)
            msgBox.setText("更新失败")
            msgBox.exec()

    def updatecoremsg(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("提示")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setWindowIcon(QIcon("img\logo.ico"))
        status = updatecore()
        if status == True:
            status = stopserviceonly()
            if status == True:
                status = replacecore()
                if status == True:
                    status == startserviceonly()
                    if status == True:
                        msgBox.setIcon(QMessageBox.Icon.Information)
                        msgBox.setText("更新失败")
                        msgBox.exec()
                    else:
                        status = stopservice()
                        msgBox.setIcon(QMessageBox.Icon.Critical)
                        msgBox.setText("更新成功，服务无法启动")
                        msgBox.exec()
                else:
                    status = stopservice()
                    msgBox.setIcon(QMessageBox.Icon.Warning)
                    msgBox.setText("无法替换Clash文件，请自行tmp文件夹替换")
                    msgBox.exec()
            else:
                status = stopservice()
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setText("更新失败，服务无法停止")
                msgBox.exec()
        else:
            status = stopservice()
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setText("更新失败，服务无法停止")
            msgBox.exec()

    def yacdopenmsg(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("提示")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setWindowIcon(QIcon("img\logo.ico"))
        status = yacdopen()
        if status == True:
            return
        else:
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setText("意外错误")
            msgBox.exec()

    def quit(self):
        # 退出程序
        QApplication.quit()