import sys
import os

from time import sleep
from PyQt5.Qt import *


class Timing(QThread):
    signal = pyqtSignal()
    def __init__(self, time, parent=None):
        super().__init__(parent=parent)
        self.time = time
    
    def run(self):
        while self.time:
            sleep(1)
            self.time -= 1
        self.signal.emit()


class Win(QWidget):
    """
    自定义一个窗口
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.thread_timing = Timing(3)
        self.asset_path = os.path.join(os.path.dirname(__file__), 'assets')

        self.init_ui()
        self.thread_timing.signal.connect(self.timing)
        self.thread_timing.start()

    def init_ui(self):
        self.setGeometry(0, 0, 300, 300)
        self.label = QLabel(self);
        self.gif = QMovie(os.path.join(self.asset_path,  'loading.gif'))
        self.label.setMovie(self.gif)
        self.gif.start()

    def timing(self):
        QMessageBox.information(self, 'tips', '加载成功', QMessageBox.Yes)
        exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Win()
    w.show()

    exit(app.exec_())