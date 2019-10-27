import sys

from PyQt5.QtWidgets import QApplication
from qt_ui.mymainwindow import MyMainWindow
from qt_ui.myranklist import MyRankList
from qt_ui.myread import MyRead


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MyMainWindow()
    list_win = MyRankList()
    read_win = MyRead()
    main_win.show()
    main_win.open_signal.connect(list_win.show_win)
    list_win.back_signal.connect(main_win.show)
    list_win.read_signal.connect(read_win.show_win)

    sys.exit(app.exec_())