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
        self.title_buttons = []
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
            button.clicked.connect(lambda: self.choose_novel(i))
            self.title_buttons.append(button)
            self.verticalLayout.addWidget(button)

    def add_grid_buttons(self):
        pass

    def add_connetc(self):
        self.pushButton_quit.clicked.connect(self.back_to_main)

    def choose_novel(self, select_index):
        self.jianjie.clear()
        title = self.list_inf[self.current_index][self.current_time_name[self.current_time]][select_index]['title']
        link = self.list_inf[self.current_index][self.current_time_name[self.current_time]][select_index]['link']
        novel_getter = DownloadNovel(title, link)
        introduction = novel_getter.get_novel_introduction()
        print(title, link)
        self.label_title.setText(title)
        self.label_author.setText(introduction[0])
        self.jianjie.append(introduction[1])
        self.set_picture(novel_getter.get_novel_image())

    def set_picture(self, pic_name):
        pixmap = QtGui.QPixmap(pic_name)
        self.label_picture.setPixmap(pixmap)

    def show_win(self, list_inf):
        self.current_index = list(list_inf.keys())[0]
        self.label_list_name.setText(self.rank_lists[self.current_index])
        self.setWindowTitle(self.rank_lists[self.current_index])
        self.list_inf = list_inf
        self.add_connetc()
        self.add_buttons()
        if not self.isVisible():
            self.show()
        print(list_inf)

    def init(self):
        self.label_picture.setText('')
        self.label_author.setText('')
        self.label_title.setText('')

    def back_to_main(self):
        if self.isVisible():
            self.back_signal.emit()
            self.hide()