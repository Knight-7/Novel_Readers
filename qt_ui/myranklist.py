import os
import platform
import re
import shutil

from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from qt_ui.ranklist import Ui_Widget
from PyQt5.QtCore import pyqtSignal
from web_craw.download_novel import DownloadNovel
from web_craw.download_novel import get_novel_picture
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from time import sleep


class AThread(QtCore.QThread):
    """QT的多线程"""

    finish_signal = pyqtSignal(list, list)

    def __init__(self, title, link):
        super(AThread, self).__init__()
        self.title = title
        self.link = link

    def run(self):
        novel_getter = DownloadNovel(self.title, self.link)
        introduction = novel_getter.get_novel_introduction()
        chapter = novel_getter.get_novel_chapter()
        self.finish_signal.emit(introduction, chapter)


class PictureThread(QtCore.QThread):
    """获得图片的线程"""
    def __init__(self, novel_inf):
        super(PictureThread, self).__init__()
        self.novel_inf = novel_inf
        self.current_time_name = ['总排名', '周排名', '月排名', '日排名']
        self.executor = ThreadPoolExecutor(5)
        self.futures = []

    def close_thread(self):
        def close():
            for future in self.futures:
                future.cancel()
            self.executor.shutdown()
        Thread(target=close).start()

    def run(self):
        if platform.system() == 'Windows':
            if not os.path.exists('C:/tmp_pic'):
                os.mkdir('C:/tmp_pic')
        elif platform.system() == 'Linux':
            if not os.path.exists('/home/knight/tmp_pic'):
                os.mkdir('/home/knight/tmp_pic')
        for name in self.current_time_name:
            for inf in self.novel_inf[name]:
                self.futures.append(self.executor.submit(
                    get_novel_picture, inf['link'], inf['title']))


class MyRankList(QWidget, Ui_Widget):
    """排行榜的类"""

    read_signal = pyqtSignal(list)
    back_signal = pyqtSignal()
    close_thread_signal = pyqtSignal()

    def __init__(self):
        super(MyRankList, self).__init__()
        self.setupUi(self)
        self.load_inf_thread = None                                     # 加载小说的线程
        self.picture_get_thread = None                             # 读取图片的线程
        self.title = None                                               # 当前正在看的小说题目
        self.link = None                                                # 当前正在看的小说的题目
        self.list_inf = None                                            # 整个榜单的书名与链接
        self.current_chapter_index = 0                                  # 当前的页数
        self.current_index = None                                       # 当前选择的榜单的序号
        self.title_buttons = {}                                         # 左侧放小说名字的按钮
        self.grid_buttons = []                                          # 表格里的章节按钮
        self.current_time = 0                                           # 当前是什么排名的榜单（总排名。。。）
        self.novel_chapter = None                                       # 小说的章节名称
        self.chapters = None                                            # 某一页的小说章节
        self.length = 0                                                 # 小说章节页数
        self.picture_path = None
        self.current_time_name = ['总排名', '周排名', '月排名', '日排名']
        self.rank_lists = ['玄幻.奇幻小说排行榜', '修真.仙侠小说排行榜',
                           '都市.青春小说排行榜', '历史.穿越小说排行榜',
                           '全部小说排行榜', '全本小说排行榜',
                           '科技.灵异小说排行榜', '网游.竞技小说排行榜']
        self.set_picture_path()
        self.add_buttons()
        self.add_grid_buttons()
        self.setFixedSize(self.size())
        for i in range(8):
            for j in range(4):
                self.grid_buttons[i][j].setVisible(False)

    def set_picture_path(self):
        if platform.system() == 'Windows':
            self.picture_path = 'C:/tmp_pic/'
        elif platform.system() == 'Linux':
            self.picture_path = '/home/knight/tmp_pic/'

    def add_buttons(self):
        for i in range(20):
            button = QPushButton()
            button.setText(' ')
            button.setFlat(True)
            button.setStyleSheet('text-align:left;')
            self.title_buttons[i] = button
            self.verticalLayout.addWidget(button)

    def add_grid_buttons(self):
        for i in range(8):
            tmp_list = []
            for j in range(4):
                button = QPushButton()
                button.setText(' ')
                tmp_list.append(button)
                self.gridLayout.addWidget(button, i + 1, j + 1)
            self.grid_buttons.append(tmp_list)

    def set_grid_button_name(self):
        for i in range(8):
            for j in range(4):
                self.grid_buttons[i][j].setVisible(True)
        if self.current_chapter_index < self.length:
            self.chapters = self.novel_chapter[self.current_chapter_index * 32:
                                          self.current_chapter_index * 32 + 32]
            index = 0
            for i in range(8):
                for j in range(4):
                    if ' ' in self.chapters[index][1]:
                        self.grid_buttons[i][j].setText(self.chapters[index][1][: self.chapters[index][1].index(' ')])
                    elif '：' in self.chapters[index][1]:
                        self.grid_buttons[i][j].setText(self.chapters[index][1][: self.chapters[index][1].index('：')])
                    index += 1
        else:
            self.chapters = self.novel_chapter[self.current_chapter_index * 32:]
            index = 0
            for i in range(8):
                for j in range(4):
                    if ' ' in self.chapters[index][1]:
                        self.grid_buttons[i][j].setText(self.chapters[index][1][: self.chapters[index][1].index(' ')])
                    elif '：' in self.chapters[index][1]:
                        self.grid_buttons[i][j].setText(self.chapters[index][1][: self.chapters[index][1].index('：')])
                    index += 1
                    if index == len(self.chapters):
                        for k in range(j + 1, 4):
                            self.grid_buttons[i][k].setVisible(False)
                        for k in range(i + 1, 8):
                            for l in range(4):
                                self.grid_buttons[k][l].setVisible(False)
                        return

    def add_vertical_connection(self):
        self.pushButton_quit.clicked.connect(self.back_to_main)
        self.title_buttons[0].clicked.connect(lambda: self.choose_novel(0))
        self.title_buttons[1].clicked.connect(lambda: self.choose_novel(1))
        self.title_buttons[2].clicked.connect(lambda: self.choose_novel(2))
        self.title_buttons[3].clicked.connect(lambda: self.choose_novel(3))
        self.title_buttons[4].clicked.connect(lambda: self.choose_novel(4))
        self.title_buttons[5].clicked.connect(lambda: self.choose_novel(5))
        self.title_buttons[6].clicked.connect(lambda: self.choose_novel(6))
        self.title_buttons[7].clicked.connect(lambda: self.choose_novel(7))
        self.title_buttons[8].clicked.connect(lambda: self.choose_novel(8))
        self.title_buttons[9].clicked.connect(lambda: self.choose_novel(9))
        self.title_buttons[10].clicked.connect(lambda: self.choose_novel(10))
        self.title_buttons[11].clicked.connect(lambda: self.choose_novel(11))
        self.title_buttons[12].clicked.connect(lambda: self.choose_novel(12))
        self.title_buttons[13].clicked.connect(lambda: self.choose_novel(13))
        self.title_buttons[14].clicked.connect(lambda: self.choose_novel(14))
        self.title_buttons[15].clicked.connect(lambda: self.choose_novel(15))
        self.title_buttons[16].clicked.connect(lambda: self.choose_novel(16))
        self.title_buttons[17].clicked.connect(lambda: self.choose_novel(17))
        self.title_buttons[18].clicked.connect(lambda: self.choose_novel(18))
        self.title_buttons[19].clicked.connect(lambda: self.choose_novel(19))

    def add_grid_connection(self):
        self.grid_buttons[0][0].clicked.connect(lambda: self.read_novel(0))
        self.grid_buttons[0][1].clicked.connect(lambda: self.read_novel(1))
        self.grid_buttons[0][2].clicked.connect(lambda: self.read_novel(2))
        self.grid_buttons[0][3].clicked.connect(lambda: self.read_novel(3))
        self.grid_buttons[1][0].clicked.connect(lambda: self.read_novel(4))
        self.grid_buttons[1][1].clicked.connect(lambda: self.read_novel(5))
        self.grid_buttons[1][2].clicked.connect(lambda: self.read_novel(6))
        self.grid_buttons[1][3].clicked.connect(lambda: self.read_novel(7))
        self.grid_buttons[2][0].clicked.connect(lambda: self.read_novel(8))
        self.grid_buttons[2][1].clicked.connect(lambda: self.read_novel(9))
        self.grid_buttons[2][2].clicked.connect(lambda: self.read_novel(10))
        self.grid_buttons[2][3].clicked.connect(lambda: self.read_novel(11))
        self.grid_buttons[3][0].clicked.connect(lambda: self.read_novel(12))
        self.grid_buttons[3][1].clicked.connect(lambda: self.read_novel(13))
        self.grid_buttons[3][2].clicked.connect(lambda: self.read_novel(14))
        self.grid_buttons[3][3].clicked.connect(lambda: self.read_novel(15))
        self.grid_buttons[4][0].clicked.connect(lambda: self.read_novel(16))
        self.grid_buttons[4][1].clicked.connect(lambda: self.read_novel(17))
        self.grid_buttons[4][2].clicked.connect(lambda: self.read_novel(18))
        self.grid_buttons[4][3].clicked.connect(lambda: self.read_novel(19))
        self.grid_buttons[5][0].clicked.connect(lambda: self.read_novel(20))
        self.grid_buttons[5][1].clicked.connect(lambda: self.read_novel(21))
        self.grid_buttons[5][2].clicked.connect(lambda: self.read_novel(22))
        self.grid_buttons[5][3].clicked.connect(lambda: self.read_novel(23))
        self.grid_buttons[6][0].clicked.connect(lambda: self.read_novel(24))
        self.grid_buttons[6][1].clicked.connect(lambda: self.read_novel(25))
        self.grid_buttons[6][2].clicked.connect(lambda: self.read_novel(26))
        self.grid_buttons[6][3].clicked.connect(lambda: self.read_novel(27))
        self.grid_buttons[7][0].clicked.connect(lambda: self.read_novel(28))
        self.grid_buttons[7][1].clicked.connect(lambda: self.read_novel(29))
        self.grid_buttons[7][2].clicked.connect(lambda: self.read_novel(30))
        self.grid_buttons[7][3].clicked.connect(lambda: self.read_novel(31))

    def choose_novel(self, select_index):
        self.title = self.list_inf[self.current_index][self.current_time_name[self.current_time]][select_index]['title']
        self.link = self.list_inf[self.current_index][self.current_time_name[self.current_time]][select_index]['link']
        self.get_novel_inf(self.title, self.link)

    def get_novel_inf(self, title, link):
        self.load_inf_thread = AThread(title, link)
        self.load_inf_thread.finish_signal.connect(self.set_novel_inf)
        self.load_inf_thread.start()

    def set_novel_inf(self, introduction, chapter):
        for i in range(8):
            for j in range(4):
                self.grid_buttons[i][j].setVisible(True)
        self.label_title.setText(self.title)
        self.label_author.setText(introduction[0])
        self.jianjie.clear()
        self.jianjie.append(introduction[1])
        self.set_picture(self.title)
        self.novel_chapter = chapter
        self.length = len(self.novel_chapter) // 32 - 1 \
            if len(self.novel_chapter) % 32 == 0 else len(self.novel_chapter) // 32
        self.label_total_page.setText('/' + str(self.length))
        self.lineEdit_page.setText('1')
        self.set_grid_button_name()
        sleep(0.2)

    def set_picture(self, pic_name):
        pic_name = re.sub('\d', '', pic_name)
        pixmap = QtGui.QPixmap(self.picture_path + pic_name + '.jpg')
        self.label_picture.setPixmap(pixmap)
        self.label_picture.setScaledContents(True)

    def show_win(self, list_inf):
        self.list_inf = list_inf
        self.current_index = list(list_inf.keys())[0]
        self.init()
        self.add_vertical_connection()
        self.add_grid_connection()
        self.save_pictures()
        if not self.isVisible():
            self.show()

    def save_pictures(self):
        self.picture_get_thread = PictureThread(self.list_inf[self.current_index])
        self.close_thread_signal.connect(self.picture_get_thread.close_thread)
        self.picture_get_thread.start()

    def change_title_list(self, index):
        self.pushButton_total.setDisabled(False)
        self.pushButton_week.setDisabled(False)
        self.pushButton_month.setDisabled(False)
        self.pushButton_day.setDisabled(False)
        self.current_time = index
        if index == 0:
            self.pushButton_total.setDisabled(True)
        elif index == 1:
            self.pushButton_week.setDisabled(True)
        elif index == 2:
            self.pushButton_month.setDisabled(True)
        else:
            self.pushButton_day.setDisabled(True)
        for i in range(20):
            self.title_buttons[i].setText(self.list_inf[self.current_index]
                                          [self.current_time_name[self.current_time]][i]['title'])

    def init(self):
        self.label_picture.setText('')
        self.label_author.setText('')
        self.label_title.setText('')
        self.label_total_page.setText('')
        self.pushButton_total.setDisabled(True)
        self.label_list_name.setText(self.rank_lists[self.current_index])
        self.setWindowTitle(self.rank_lists[self.current_index])
        self.pushButton_total.clicked.connect(lambda: self.change_title_list(0))
        self.pushButton_week.clicked.connect(lambda: self.change_title_list(1))
        self.pushButton_month.clicked.connect(lambda: self.change_title_list(2))
        self.pushButton_day.clicked.connect(lambda: self.change_title_list(3))
        self.pushButton_next_page.clicked.connect(lambda: self.change_page(2))
        self.pushButton_pre_page.clicked.connect(lambda: self.change_page(1))
        for i in range(20):
            self.title_buttons[i].setText(self.list_inf[self.current_index]
                                          [self.current_time_name[self.current_time]][i]['title'])

    def change_page(self, choose):
        if choose == 1 and self.current_chapter_index > 0:
            self.current_chapter_index -= 1
        elif choose == 1 and self.current_chapter_index == 0:
            QMessageBox.about(self, '提示', '已经第一页了')
        elif choose == 2 and self.current_chapter_index < self.length:
            self.current_chapter_index += 1
        else:
            QMessageBox.about(self, '提示', '已经最后一页了')
        self.lineEdit_page.setText(str(self.current_chapter_index))
        self.set_grid_button_name()

    def back_to_main(self):
        for i in range(8):
            for j in range(4):
                self.grid_buttons[i][j].setVisible(False)
        self.jianjie.clear()
        self.label_picture.setPixmap(QtGui.QPixmap(''))
        self.close_thread_signal.emit()
        if self.isVisible():
            self.back_signal.emit()
            self.hide()

    def read_novel(self, index):
        self.read_signal.emit(list(self.chapters[index]))

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提问', '是否要退出程序？',
                                     QMessageBox.Yes|QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close_thread_signal.emit()
            if os.path.exists(self.picture_path[:-1]):
                shutil.rmtree(self.picture_path[:-1])
            event.accept()
        else:
            event.ignore()