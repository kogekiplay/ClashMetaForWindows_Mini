
# 定义全局快捷键
import global_hotkeys as hotkey

# 实现系统托盘程序
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QWidget
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Signal, Slot
import img.app_icon_rc as app_rc # 由pyside6-rcc生成的资源文件

class MySysTrayWidget(QWidget):
    # 自定义个信号
    hotkeyed = Signal(bool)

    def __init__(self, ui=None, app=None, window=None):
        QWidget.__init__(self)  # 必须调用，否则信号系统无法启用

        # 私有变量
        self.__ui = ui
        self.__app = app
        self.__window = window
        self.__ui.setupUi(self.__window)

        # 配置系统托盘
        self.__trayicon = QSystemTrayIcon(self)
        self.__trayicon.setIcon(QIcon('img/logo.ico'))
        self.__trayicon.setToolTip('Clash Meta For Windows Mini\n热键Ctrl+Alt+M')

        # 创建托盘的右键菜单
        self.__traymenu = QMenu()
        self.__trayaction = []
        self.addTrayMenuAction('显示主界面', self.showUserInterface)
        self.addTrayMenuAction('退出', self.quit)
        self.__trayicon.activated.connect(self.iconActivated)

        # 配置菜单并显示托盘
        self.__trayicon.setContextMenu(self.__traymenu) #把tpMenu设定为托盘的右键菜单
        self.__trayicon.show()  #显示托盘   

        # These take the format of [<key list>, <keydown handler callback>, <keyup handler callback>]
        self.hotkey_bindings = [
            [["control", "alt", "m"], None, self.wakeHotkey],
        ]

        hotkey.register_hotkeys(self.hotkey_bindings)
        hotkey.start_checking_hotkeys()

        # 连接信号
        self.__ui.pushButton.clicked.connect(self.hideUserInterface)
        self.hotkeyed.connect(self.onHotkey)

        # 默认隐藏界面
        self.hideUserInterface()

    def __del__(self):
        pass

    def addTrayMenuAction(self, text='empty', callback=None):
        a = QAction(text, self)
        a.triggered.connect(callback)
        self.__traymenu.addAction(a)
        self.__trayaction.append(a)

    def iconActivated(self,reason):
        if reason == QSystemTrayIcon.DoubleClick or reason == QSystemTrayIcon.Trigger:
            if self.__trayicon.isVisible() or self.__trayicon.isMinimized():
                self.showUserInterface()
                
    def quit(self):
        # 真正的退出
        self.__app.exit()
    
    def showUserInterface(self):
        self.__window.show()

    def hideUserInterface(self):
        self.__window.hide()

    def wakeHotkey(self):
        self.hotkeyed.emit(self.__window.isVisible())

    @Slot(bool)
    def onHotkey(self, visible):
        print('here', visible)
        if visible:
            self.hideUserInterface()
        else:
            self.showUserInterface()
