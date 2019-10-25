from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from qt_ui.ranklist import Ui_Widget
from PyQt5.QtCore import pyqtSignal
from web_craw.download_novel import DownloadNovel


class MyRankList(QWidget, Ui_Widget):
    """排行榜的类"""

    back_signal = pyqtSignal()

    def __init__(self):
        super(MyRankList, self).__init__()
        self.setupUi(self)
        self.list_inf = None
        self.current_index = None
        self.title_buttons = {}
        self.grid_buttons = []
        self.current_time = 0
        self.current_time_name = ['总排名', '周排名', '月排名', '日排名']
        self.rank_lists = ['玄幻.奇幻小说排行榜', '修真.仙侠小说排行榜',
                           '都市.青春小说排行榜', '历史.穿越小说排行榜',
                           '全部小说排行榜', '全本小说排行榜',
                           '科技.灵异小说排行榜', '网游.竞技小说排行榜']

    def add_buttons(self):
        for i in range(20):
            button = QPushButton()
            button.setText(self.list_inf[self.current_index]['总排名'][i]['title'])
            button.setFlat(True)
            button.setStyleSheet('text-align:left;')
            self.title_buttons[i] = button
            self.verticalLayout.addWidget(button)

    def add_grid_buttons(self):
        pass

    def add_connetc(self):
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

    def choose_novel(self, select_index):
        self.jianjie.clear()
        title = self.list_inf[self.current_index][self.current_time_name[self.current_time]][select_index]['title']
        link = self.list_inf[self.current_index][self.current_time_name[self.current_time]][select_index]['link']
        novel_getter = DownloadNovel(title, link)
        introduction = novel_getter.get_novel_introduction()
        self.label_title.setText(title)
        self.label_author.setText(introduction[0])
        self.jianjie.append(introduction[1])
        self.set_picture(novel_getter.get_novel_image())

    def set_picture(self, pic_name):
        pixmap = QtGui.QPixmap(pic_name)
        self.label_picture.setPixmap(pixmap)
        self.label_picture.setScaledContents(True)

    def show_win(self, list_inf):
        self.init()
        self.current_index = list(list_inf.keys())[0]
        self.label_list_name.setText(self.rank_lists[self.current_index])
        self.setWindowTitle(self.rank_lists[self.current_index])
        self.list_inf = list_inf
        self.add_buttons()
        self.add_connetc()
        if not self.isVisible():
            self.show()

    def init(self):
        self.label_picture.setText('')
        self.label_author.setText('')
        self.label_title.setText('')

    def back_to_main(self):
        if self.isVisible():
            self.back_signal.emit()
            self.hide()