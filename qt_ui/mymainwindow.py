import platform
import os
import shutil

from qt_ui.mainwindow import Ui_MainWidget
from PyQt5.Qt import *
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
        self.picture_path = None
        self.set_picture_path()
        self.setFixedSize(self.size())
        self.set_sheet_stytle()

        # icon = QIcon('a10.ico')
        # self.setWindowIcon(icon)

    def set_sheet_stytle(self):
        path = os.path.dirname(os.path.dirname(__file__))
        with open(path + '/assets/qss/black.qss', 'r', encoding='utf8') as f:
            qss = f.read()
        self.setStyleSheet(qss)

    def set_picture_path(self):
        if platform.system() == 'Windows':
            self.picture_path = 'C:/tmp_pic'
        elif platform.system() == 'Linux':
            self.picture_path = '/home/knight/tmp_pic'

    def get_list(self):
        novel = []
        for rank in self.list_getter.get_novel_list():
            novel.append(rank)
        self.list = novel

    def choose(self, index):
        self.open_signal.emit({index: self.list[index]})
        self.hide()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提问', '是否要退出程序？',
                                     QMessageBox.Yes|QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            if os.path.exists(self.picture_path):
                shutil.rmtree(self.picture_path)
            event.accept()
        else:
            event.ignore()