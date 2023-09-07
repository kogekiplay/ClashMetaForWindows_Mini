# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'textline.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QSettings)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QLabel,
    QLineEdit, QSizePolicy, QWidget,QMessageBox)
from foo.test.downconfig import downlaod_config

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(325, 113)
        Form.setStyleSheet(u"QLabel {\n"
"	color: #6f9aca;\n"
"}")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 40, 301, 31))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 161, 31))
        self.buttonBox = QDialogButtonBox(Form)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(160, 80, 156, 24))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        # 处理点击事件
        self.buttonBox.accepted.connect(self.on_ok_clicked)
        self.buttonBox.rejected.connect(self.close)
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u63d0\u793a", None))
        Form.setWindowIcon(QIcon("img\logo.ico"))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u8bf7\u8f93\u5165\u4f60\u7684\u8ba2\u9605\u94fe\u63a5\uff1a</span></p></body></html>", None))
    # retranslateUi

    def on_ok_clicked(self):
        proxylink = self.lineEdit.text()
        if proxylink: # 如果proxylink不是空字符串
            status=downlaod_config(proxylink)
            if isinstance(status, str):
                QMessageBox.warning(self, "警告", status) # 弹出警告消息框
            elif status == True:
                QMessageBox.information(self, "提示", "下载成功") # 弹出警告消息框
                # 创建一个QSettings对象，并获取保存的设置值，指定ini格式和自定义文件名
                settings = QSettings("config/config.ini", QSettings.IniFormat)
                settings.setValue("url", proxylink)
                self.close() # 关闭窗口
            else:
                QMessageBox.warning(self, "警告", "不是合法链接") # 弹出警告消息框
        else: # 如果proxylink是空字符串
            QMessageBox.warning(self, "警告", "请输入订阅链接") # 弹出警告消息框