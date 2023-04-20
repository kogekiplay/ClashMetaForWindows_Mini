import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from foo.test.tunmode import proxyswitch
from foo.test.service import startservice,stopservice,stopserviceonly,startserviceonly
from foo.test.update import updateyacd,updatecore,replacecore
from foo.test.yacdopen import yacdopen

StyleSheet = """
QPushButton {
    color:#ffffff; /*文字颜色*/
    background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop:0 #aa55ff, stop: 1 #1296db);/*背景色*/
    border-style:outset; /*边框风格*/
    border-width:2px;/*边框宽度*/
    border-color:#0055ff; /*边框颜色*/
    border-radius:10px; /*边框倒角*/
    font:bold 14px; /*字体*/
    font-family: Segoe UI;
    min-width:100px;/*控件最小宽度*/
    min-height:20px;/*控件最小高度*/
    padding:4px;/*内边距*/

}
"""



# 重写QSystemTrayIcon类，设置托盘图标的属性和事件
class TrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self,MainWindow,parent=None):
        super(TrayIcon, self).__init__(parent)
        self.ui = MainWindow # 传入主窗口对象
        self.createMenu() # 创建菜单

    def createMenu(self):
        self.menu = QtWidgets.QMenu() # 创建菜单对象
        self.setToolTip("Clash Meta For Windows Mini")
        self.showAction = QtWidgets.QAction("显示主界面", self, triggered=self.show_window) # 创建显示主界面的动作
        self.quitAction = QtWidgets.QAction("退出", self, triggered=self.quit) # 创建退出程序的动作
        self.menu.addAction(self.showAction) # 添加显示主界面的动作到菜单
        self.menu.addAction(self.quitAction) # 添加退出程序的动作到菜单
        self.setContextMenu(self.menu) # 设置托盘图标的右键菜单为self.menu
        # 设置图标
        self.setIcon(QtGui.QIcon("img\logo.ico")) # 设置托盘图标为logo.ico
        self.icon = self.MessageIcon()
        # 把鼠标点击图标的信号和槽连接
        self.activated.connect(self.onIconClicked)

    # 点击托盘图标，切换主窗口的显示或隐藏状态
    def onIconClicked(self, reason):
        if reason == 2 or reason == 3: # 鼠标左键单击或双击
            if self.ui.isMinimized() or not self.ui.isVisible():
                # 如果窗口是最小化或者隐藏状态，则显示窗口并激活它
                self.ui.showNormal()
                self.ui.activateWindow()
            else:
                # 如果窗口是正常显示状态，则隐藏窗口
                self.ui.hide()

    # 显示主窗口
    def show_window(self):
        if self.ui.isMinimized() or not self.ui.isVisible():
            # 如果窗口是最小化或者隐藏状态，则显示窗口并激活它
            self.ui.showNormal()
            self.ui.activateWindow()

    # 退出程序
    def quit(self):
        QtWidgets.qApp.quit()


class MyWindow(QWidget):
    def __init__(self,parent=None):
        super(MyWindow,self).__init__(parent)
        self.setWindowIcon(QIcon("img\logo.ico"))
        self.setWindowTitle("CMFW mini")
        self.resize(400,200)
        self.btn1=QPushButton(self)
        self.btn1.setText("Clash Meta服务打开")
        self.btn1.clicked.connect(self.msg1)
        layout=QVBoxLayout()

        self.btn2=QPushButton(self)
        self.btn2.setText("Clash Meta服务关闭")
        self.btn2.clicked.connect(self.msg2)

        self.btn3=QPushButton(self)
        self.btn3.setText("Tun/系统代理切换")
        self.btn3.clicked.connect(self.msg3)

        self.btn4=QPushButton(self)
        self.btn4.setText("更新Yacd-Meta")
        self.btn4.clicked.connect(self.msg4)

        self.btn5=QPushButton(self)
        self.btn5.setText("更新到最新Alpha核心")
        self.btn5.clicked.connect(self.msg5)

        self.btn6=QPushButton(self)
        self.btn6.setText("打开Yacd-Meta面板")
        self.btn6.clicked.connect(self.msg6)

        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)
        layout.addWidget(self.btn5)
        layout.addWidget(self.btn6)
        self.setLayout(layout)


    def msg1(self):
        #使用infomation信息框
        status = startservice()
        if status == True:
            QMessageBox.information(self,"提示","服务安装并启动成功，自行检查log文件夹",QMessageBox.Ok)
        elif status == False:
            QMessageBox.critical(self,"提示","服务启动失败",QMessageBox.Ok)
        elif status == "not exist":
            QMessageBox.warning(self,"提示","\"config.yaml\"不存在",QMessageBox.Ok)
        elif status == "no permission":
            QMessageBox.critical(self,"提示","\"config.yaml\"无法写入",QMessageBox.Ok)
        elif status == "error":
            QMessageBox.critical(self,"提示","发生了意料之外的错误",QMessageBox.Ok)
        else:
            QMessageBox.warning(self,"提示",status,QMessageBox.Ok)

    def msg2(self):
        #使用infomation信息框
        status = stopservice()
        if status == True:
            QMessageBox.information(self,"提示","服务卸载成功",QMessageBox.Ok)
        elif status == False:
            QMessageBox.warning(self,"提示","服务卸载失败（你安装成功了吗）",QMessageBox.Ok)
    
    def msg3(self):
        #使用infomation信息框
        status = proxyswitch()
        if status == True:
            QMessageBox.information(self,"提示","tun模式已开启,系统代理已关闭",QMessageBox.Ok)
        elif status == False:
            QMessageBox.information(self,"提示","tun模式已关闭,系统代理已开启",QMessageBox.Ok)
    
    def msg4(self):
        status = updateyacd()
        if status == True:
            QMessageBox.information(self,"提示","更新成功",QMessageBox.Ok)
        else:
            QMessageBox.warning(self,"提示","更新失败",QMessageBox.Ok)

    def msg5(self):
        status = updatecore()
        if status == True:
            status = stopserviceonly()
            if status == True:
                status = replacecore()
                if status == True:
                    status == startserviceonly()
                    if status == True:
                        QMessageBox.information(self,"提示","更新成功",QMessageBox.Ok)
                    else:
                        status = stopservice()
                        QMessageBox.information(self,"提示","更新成功，服务无法启动",QMessageBox.Ok)
                else:
                    status = stopservice()
                    QMessageBox.information(self,"提示","无法替换Clash文件，请自行tmp文件夹替换",QMessageBox.Ok)
            else:
                status = stopservice()
                QMessageBox.information(self,"提示","更新失败，服务无法停止",QMessageBox.Ok)
        else:
            status = stopservice()
            QMessageBox.information(self,"提示","下载失败",QMessageBox.Ok)

    def msg6(self):
        status = yacdopen()
        if status == True:
            return
        else:
             QMessageBox.warning(self,"提示","意外错误",QMessageBox.Ok)

    # 重写关闭事件，使得关闭窗口时不是退出程序，而是隐藏窗口
    def closeEvent(self, event):
        event.ignore() # 忽略关闭事件
        self.hide() # 隐藏窗口

# 启动主窗口
def runWindow():
    app=QApplication(sys.argv)
    share = QSharedMemory()
    share.setKey("main_window")
    if share.attach():
        msg_box = QMessageBox()
        msg_box.setWindowTitle("提示")
        msg_box.setText("软件已在运行!")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.addButton("确定", QMessageBox.YesRole)
        msg_box.exec()
        sys.exit(-1)
    if share.create(1):
        app.setStyleSheet(StyleSheet)
        win=MyWindow()
        win.show()
        tray = TrayIcon(win) # 创建托盘图标对象，并传入主窗口对象
        tray.show() # 显示托盘图标
        sys.exit(app.exec_())


if __name__=="__main__":
    runWindow()