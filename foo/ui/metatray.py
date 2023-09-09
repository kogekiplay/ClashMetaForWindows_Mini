
# 定义全局快捷键
import global_hotkeys as hotkey

import os

# 实现系统托盘程序
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QWidget
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Signal, Slot, QSettings
import img.app_icon_rc as app_rc  # 由pyside6-rcc生成的资源文件
from foo.test.tunmode import switch_tun_mode, enable_default_proxy, disable_proxy
from foo.test.xdopen import xdopen

# 引入开机启动
from foo.test.autostart import getexepath, add_to_startup, remove_from_startup


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
        self.__trayicon.setToolTip(self.tr('Clash Meta For Windows Mini'))

        # 创建托盘的右键菜单
        self.__traymenu = QMenu()
        self.__trayaction = []

        # 创建一个代理菜单项，并设置为可选中的
        self.proxy_switch_action = QAction(self.tr("系统代理"), self)
        self.proxy_switch_action.setCheckable(True)
        # 连接开机自启动菜单项的触发信号到一个槽函数，用于处理设置的改变
        self.proxy_switch_action.triggered.connect(
            self.on_proxy_switch_setting_changed)

        # 创建一个Tun菜单项，并设置为可选中的
        self.tun_switch_action = QAction(self.tr("Tun 模式"), self)
        self.tun_switch_action.setCheckable(True)
        # 连接开机自启动菜单项的触发信号到一个槽函数，用于处理设置的改变
        self.tun_switch_action.triggered.connect(
            self.on_tun_mode_switch_setting_changed)

        # 创建一个开机自启动菜单项，并设置为可选中的
        self.startup_action = QAction(self.tr("开机自启动"), self)
        self.startup_action.setCheckable(True)
        # 连接开机自启动菜单项的触发信号到一个槽函数，用于处理设置的改变
        self.startup_action.triggered.connect(self.on_startup_setting_changed)

        # 创建一个dashboard菜单项
        self.dashboard_action = QAction(self.tr("打开 Dashboard"), self)
        # 连接开机自启动菜单项的触发信号到一个槽函数，用于处理设置的改变
        self.dashboard_action.triggered.connect(self.open_dashboard)

        self.addTrayMenuAction('显示主界面', self.showUserInterface)
        self.__traymenu.addAction(self.startup_action)
        self.__traymenu.addSeparator()
        self.__traymenu.addAction(self.proxy_switch_action)
        self.__traymenu.addAction(self.tun_switch_action)
        self.__traymenu.addSeparator()
        self.__traymenu.addAction(self.dashboard_action)
        self.__traymenu.addSeparator()
        self.addTrayMenuAction('退出', self.quit)
        self.__trayicon.activated.connect(self.iconActivated)

        # 配置菜单并显示托盘
        self.__trayicon.setContextMenu(self.__traymenu)  # 把tpMenu设定为托盘的右键菜单
        self.__trayicon.show()  # 显示托盘

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

    def iconActivated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick or reason == QSystemTrayIcon.Trigger:
            if self.__trayicon.isVisible() or self.__trayicon.isMinimized():
                self.showUserInterface()

    # 定义一个方法，用于注销热键
    def unregister_hotkey(self):
        # 使用global_hotkeys模块来注销热键
        hotkey.clear_hotkeys()
        hotkey.stop_checking_hotkeys()

     # 定义一个槽函数，用于处理tun模式设置的改变
    def on_tun_mode_switch_setting_changed(self):
        # 获取设置菜单项的选中状态
        checked = self.tun_switch_action.isChecked()
        # 根据选中状态显示不同的提示信息,并启停tun模式
        if checked:
            switch_tun_mode(True)
        else:
            switch_tun_mode(False)
        # 保存设置到QSettings对象中，指定ini格式和自定义文件名
        settings = QSettings("config/config.ini", QSettings.IniFormat)
        settings.setValue("tun", checked)

    # 定义一个槽函数，用于处理系统代理设置的改变

    def on_proxy_switch_setting_changed(self):
        # 获取设置菜单项的选中状态
        checked = self.proxy_switch_action.isChecked()
        if checked == True:
            self.proxy_switch_action.setChecked(checked)
        # 根据选中状态显示不同的提示信息,并启用系统代理
        if checked:
            enable_default_proxy()
        else:
            disable_proxy()
        # 保存设置到QSettings对象中，指定ini格式和自定义文件名
        settings = QSettings("config/config.ini", QSettings.IniFormat)
        settings.setValue("proxy", checked)

    # 定义一个槽函数，用于处理设置的改变
    def on_startup_setting_changed(self):
        # 获取设置菜单项的选中状态
        checked = self.startup_action.isChecked()
        exe_path = getexepath()
        # 根据选中状态显示不同的提示信息,并调用注册表函数
        if checked:
            add_to_startup(exe_path)
            self.__trayicon.showMessage(self.tr("提示"), self.tr("已开启开机自启动"))
        else:
            remove_from_startup(exe_path)
            self.__trayicon.showMessage(self.tr("提示"), self.tr("已关闭开机自启动"))
        # 保存设置到QSettings对象中，指定ini格式和自定义文件名
        settings = QSettings("config/config.ini", QSettings.IniFormat)
        settings.setValue("startup", checked)

    # Open xd dashboard
    def open_dashboard(self):
        xdopen()

    # 定义一个方法，用于恢复设置
    def restore_settings(self):
        # 创建一个QSettings对象，并获取保存的设置值，指定ini格式和自定义文件名
        settings = QSettings("config/config.ini", QSettings.IniFormat)
        startup_checked = settings.value("startup", False, type=bool)
        proxy_checked = settings.value("proxy", False, type=bool)
        tun_checked = settings.value("tun", False, type=bool)
        exe_path = getexepath()
        # 根据config恢复开机自启动注册表状态
        if startup_checked == True:
            add_to_startup(exe_path)
        # 设置开机自启动菜单项的选中状态
        elif startup_checked == False:
            remove_from_startup(exe_path)
        self.startup_action.setChecked(startup_checked)
        # 设置系统代理菜单项的选中状态
        if proxy_checked == True:
            enable_default_proxy()
        elif proxy_checked == False:
            disable_proxy()
        self.proxy_switch_action.setChecked(proxy_checked)
        # 设置tun模式菜单项的选中状态
        if tun_checked == True:
            switch_tun_mode(True)
        elif tun_checked == False:
            switch_tun_mode(False)
        self.tun_switch_action.setChecked(tun_checked)

    def quit(self):
        # 真正的退出
        self.unregister_hotkey()
        self.__app.exit()

    def showUserInterface(self):
        self.__window.show()

    def hideUserInterface(self):
        self.__window.hide()

    def wakeHotkey(self):
        self.hotkeyed.emit(self.__window.isVisible())

    @Slot(bool)
    def onHotkey(self, visible):
        if visible:
            self.hideUserInterface()
        else:
            self.showUserInterface()
