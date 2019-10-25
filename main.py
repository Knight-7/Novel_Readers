import sys

from PyQt5.QtWidgets import QApplication
from qt_ui.mymainwindow import MyMainWindow
from qt_ui.myranklist import MyRankList


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MyMainWindow()
    list_win = MyRankList()
    main_win.show()
    main_win.open_signal.connect(list_win.show_win)
    list_win.back_signal.connect(main_win.show)

    sys.exit(app.exec_())