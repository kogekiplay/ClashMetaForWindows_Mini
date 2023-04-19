import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from tunmode import proxyswitch


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
class MyWindow(QWidget):
    def __init__(self,parent=None):
        super(MyWindow,self).__init__(parent)
        self.setWindowTitle("CMFW mini")
        self.resize(400,200)
        self.btn1=QPushButton(self)
        self.btn1.setText("Tun/系统代理切换")
        self.btn1.clicked.connect(self.msg1)
        layout=QVBoxLayout()

        self.btn2=QPushButton(self)
        self.btn2.setText("更新Yacd-Meta")
        self.btn2.clicked.connect(self.msg2)

        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)

        self.setLayout(layout)

    
    def msg1(self):
        #使用infomation信息框
        status = proxyswitch()
        if status == True:
            QMessageBox.information(self,"提示","tun模式已开启,系统代理已关闭",QMessageBox.Ok)
        elif status == False:
            QMessageBox.information(self,"提示","tun模式已关闭,系统代理已开启",QMessageBox.Ok)
        
    def msg2(self):
        QMessageBox.information(self,"提示","更新成功",QMessageBox.Ok)

if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    win=MyWindow()
    win.show()
    sys.exit(app.exec_())