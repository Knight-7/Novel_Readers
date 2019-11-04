from PyQt5.QtCore import QThread, pyqtSignal
from urllib.parse import urljoin
from web_craw.download_novel import get_next_chapter, get_pre_chapter, get_novel_text


class NovelInfThread(QThread):
    """获取小说内容的线程"""

    send_inf = pyqtSignal(str, list, str)

    def __init__(self, base_url, url, pos):
        super(NovelInfThread, self).__init__()
        self.base_url = base_url
        self.url = url
        self.pos = pos

    def run(self):
        if self.pos == 1:
            url = urljoin(self.base_url, get_next_chapter(self.url))
            title, text = get_novel_text(url, 2)
            self.send_inf.emit(title, text, url)
        elif self.pos == 2:
            url = urljoin(self.base_url, get_pre_chapter(self.url))
            title, text = get_novel_text(url, 2)
            self.send_inf.emit(title, text, url)