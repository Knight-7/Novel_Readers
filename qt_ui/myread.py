from qt_ui.read import Ui_read
from PyQt5.Qt import *
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
        self.menu = None
        self.pushButton_next.clicked.connect(self.get_next)
        self.pushButton_pre.clicked.connect(self.get_pre)
        self.set_form_layout()
        self.create_menu()

        icon = QIcon('a10.ico')
        self.setWindowIcon(icon)

    def create_menu(self):
        self.textBrowser_novel_text.setContextMenuPolicy(Qt.CustomContextMenu)
        self.textBrowser_novel_text.customContextMenuRequested.connect(self.create_right_table)

    def create_right_table(self, pos):
        self.menu = QMenu()
        op1 = self.menu.addAction('夜间模式')
        op2 = self.menu.addAction('白天模式')

        action = self.menu.exec_(self.textBrowser_novel_text.mapToGlobal(pos))

        if action == op1:
            self.change_sheet(1)
        elif action == op2:
            self.change_sheet(2)

    def set_sheet_stytle(self):
        with open('qss/textbrowser.qss', 'r', encoding='utf8') as f:
            qss = f.read()
        self.setStyleSheet(qss)

    def change_sheet(self, model):
        if model == 1:
            self.set_sheet_stytle()
            self.textBrowser_novel_text.setTextColor(QColor('white'))
        elif model == 2:
            self.setStyleSheet('QWidget{ background-color: rgb(234, 234, 234);\
font: 24pt "楷体";}\
')
            self.textBrowser_novel_text.setTextColor(QColor('black'))

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