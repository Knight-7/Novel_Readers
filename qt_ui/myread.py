from qt_ui.read import Ui_read
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from web_craw.download_novel import get_novel_text
from urllib.parse import urljoin


class MyRead(QWidget, Ui_read):
    """阅读窗口"""

    back_to_list = pyqtSignal()

    def __init__(self):
        super(MyRead, self).__init__()
        self.setupUi(self)
        self.novel_inf = None
        self.novel_text = None
        self.base_url = 'http://www.xbiquge.la/'                        # 笔趣阁网址

    def show_win(self, novel_inf):
        self.novel_inf = novel_inf
        self.label_chapter.setText(self.novel_inf[1])
        self.show_novel()
        if not self.isVisible():
            self.show()

    def show_novel(self):
        url = urljoin(self.base_url, self.novel_inf[0])
        self.novel_text = get_novel_text(url, 2)
        self.textBrowser_novel_text.clear()
        for text in self.novel_text:
            self.textBrowser_novel_text.append(text)
        cursor = self.textBrowser_novel_text.textCursor()
        self.textBrowser_novel_text.moveCursor(cursor.Start)