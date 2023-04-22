import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QSharedMemory
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget,QMessageBox
import foo.ui.main as mainui
from foo.ui.metatray import MySysTrayWidget

class MyMainWindow(QMainWindow):
    # 继承一个QMainWindow，点右上角不会退出
    def __init__(self):
        QMainWindow.__init__(self)

    def closeEvent(self, event):
        # 忽略退出事件，而是隐藏到托盘
        event.ignore()
        self.hide()

# 进程锁
def runWindow():
    # 初始化应用和窗口
    app = QApplication(sys.argv)
    app.setApplicationName("cmfwmini")
    share = QSharedMemory()
    share.setKey("cmfwmini")
    if share.attach():
        msg_box = QMessageBox()
        msg_box.setWindowTitle("提示")
        msg_box.setText("软件已在运行!")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.addButton("确定", QMessageBox.YesRole)
        msg_box.exec()
        sys.exit(-1)
    if share.create(1):
        win = MyMainWindow()
        # 载入界面
        ui = mainui.Ui_MainWindow()
        ui.setupUi(win)
        # 创建系统托盘项目
        widget = MySysTrayWidget(app=app, window=win, ui=ui)
        widget.restore_settings()
        # 显示窗口
        win.show()

        # 运行应用
        sys.exit(app.exec())

if __name__ == "__main__":
    runWindow()
    