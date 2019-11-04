# coding=utf-8
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MenuDemo(QMainWindow):
    def __init__(self, parent=None):
        super(MenuDemo, self).__init__(parent)

        self.menuBar1 = self.menuBar()
        self.menuBar1.setGeometry(QRect(0, 0, 606, 26))
        self.menuBar1.setObjectName("menuBar")
        self.menuBar1.addMenu('File')

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested['QPoint'].connect(self.rightMenuShow)

    def rightMenuShow(self):
        rightMenu = QMenu(self.menuBar1)

        self.actionreboot = QAction('zhangji')
        self.actionreboot.setObjectName("actionreboot")
        self.actionreboot.setText(QCoreApplication.translate("MainWindow", "重新开机"))
        rightMenu.addAction(self.actionreboot)

        rightMenu.exec_(QCursor.pos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MenuDemo()
    demo.show()
    sys.exit(app.exec_())