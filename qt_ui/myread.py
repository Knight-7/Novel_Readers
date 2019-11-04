from qt_ui.read import Ui_read
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from web_craw.download_novel import get_novel_text
from urllib.parse import urljoin
from threads.read_thread import NovelInfThread


class MyRead(QWidget, Ui_read):
    """阅读窗口"""

    back_to_list = pyqtSignal()

    def __init__(self):
        super(MyRead, self).__init__()
        self.setupUi(self)
        self.novel_inf = None
        self.novel_inf_thread = None
        self.novel_text = None
        self.base_url = 'http://www.xbiquge.la/'                        # 笔趣阁网址
        self.url = None
        self.chapter_title = None
        self.pushButton_next.clicked.connect(self.get_next)
        self.pushButton_pre.clicked.connect(self.get_pre)
        self.set_form_layout()

    def set_form_layout(self):
        global_layout = QVBoxLayout()
        wg1 = QWidget()
        wg2 = QWidget()
        h_layout1 = QHBoxLayout()
        h_layout2 = QHBoxLayout()
        h_layout1.setContentsMargins(20, 20, 20, 20)
        sapcer1 = QSpacerItem(300, 15)
        sapcer2 = QSpacerItem(300, 15)
        h_layout1.addWidget(self.pushButton_pre)
        h_layout1.addItem(sapcer1)
        h_layout1.addWidget(self.label_chapter)
        h_layout1.addItem(sapcer2)
        h_layout1.addWidget(self.pushButton_next)
        h_layout2.addWidget(self.textBrowser_novel_text)
        wg1.setLayout(h_layout1)
        wg2.setLayout(h_layout2)
        global_layout.addWidget(wg1)
        global_layout.addWidget(wg2)
        self.setLayout(global_layout)

    def show_win(self, novel_inf):
        self.novel_inf = novel_inf
        self.url = urljoin(self.base_url, self.novel_inf[0])
        self.chapter_title, self.novel_text = get_novel_text(self.url, 2)
        self.show_novel(self.chapter_title, self.novel_text, self.url)
        if not self.isVisible():
            self.show()

    def show_novel(self, title, text, url):
        self.url = url
        self.chapter_title = title
        self.novel_text = text
        self.label_chapter.setText(self.chapter_title)
        self.textBrowser_novel_text.clear()
        for text in self.novel_text:
            self.textBrowser_novel_text.append(text)
        cursor = self.textBrowser_novel_text.textCursor()
        self.textBrowser_novel_text.moveCursor(cursor.Start)

    def get_next(self):
        self.novel_inf_thread = NovelInfThread(self.base_url, self.url, 1)
        self.novel_inf_thread.send_inf.connect(self.show_novel)
        self.novel_inf_thread.start()

    def get_pre(self):
        self.novel_inf_thread = NovelInfThread(self.base_url, self.url, 2)
        self.novel_inf_thread.send_inf.connect(self.show_novel)
        self.novel_inf_thread.start()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提问', '是否要退出阅读？',
                                     QMessageBox.Yes|QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()