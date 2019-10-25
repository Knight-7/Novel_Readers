from PyQt5.QtWidgets import *
from qt_ui.mainwindow import Ui_MainWidget
from PyQt5.QtCore import pyqtSignal
from web_craw.download_list import DownloadList


class MyMainWindow(QWidget, Ui_MainWidget):
    """主窗口类"""

    open_signal = pyqtSignal(dict)

    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.list = None
        self.list_getter = DownloadList()
        self.get_list()

    def get_list(self):
        novel = []
        for rank in self.list_getter.get_novel_list():
            novel.append(rank)
        self.list = novel

    def choose(self, index):
        self.open_signal.emit({index: self.list[index]})
        self.hide()