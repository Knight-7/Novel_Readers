import os
import platform

from PyQt5.QtCore import *
from concurrent.futures import ThreadPoolExecutor
from web_craw.download_novel import DownloadNovel, get_novel_picture
from threading import Thread


class AThread(QThread):
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


class PictureThread(QThread):
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