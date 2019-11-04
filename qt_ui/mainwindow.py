# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(400, 600)
        self.BtnFantsy = QtWidgets.QPushButton(MainWidget)
        self.BtnFantsy.setGeometry(QtCore.QRect(40, 50, 130, 50))
        self.BtnFantsy.setObjectName("BtnFantsy")
        self.BtnGod = QtWidgets.QPushButton(MainWidget)
        self.BtnGod.setGeometry(QtCore.QRect(40, 200, 130, 50))
        self.BtnGod.setObjectName("BtnGod")
        self.BtnCTY = QtWidgets.QPushButton(MainWidget)
        self.BtnCTY.setGeometry(QtCore.QRect(40, 350, 130, 50))
        self.BtnCTY.setObjectName("BtnCTY")
        self.BtnHistory = QtWidgets.QPushButton(MainWidget)
        self.BtnHistory.setGeometry(QtCore.QRect(40, 500, 130, 50))
        self.BtnHistory.setObjectName("BtnHistory")
        self.BtnAll = QtWidgets.QPushButton(MainWidget)
        self.BtnAll.setGeometry(QtCore.QRect(230, 500, 130, 50))
        self.BtnAll.setObjectName("BtnAll")
        self.BtnComplete = QtWidgets.QPushButton(MainWidget)
        self.BtnComplete.setGeometry(QtCore.QRect(230, 350, 130, 50))
        self.BtnComplete.setObjectName("BtnComplete")
        self.BtnStrange = QtWidgets.QPushButton(MainWidget)
        self.BtnStrange.setGeometry(QtCore.QRect(230, 200, 130, 50))
        self.BtnStrange.setObjectName("BtnStrange")
        self.BtnGame = QtWidgets.QPushButton(MainWidget)
        self.BtnGame.setGeometry(QtCore.QRect(230, 50, 130, 50))
        self.BtnGame.setObjectName("BtnGame")
        self.label = QtWidgets.QLabel(MainWidget)
        self.label.setGeometry(QtCore.QRect(220, 0, 111, 61))
        self.label.setObjectName("label")

        self.retranslateUi(MainWidget)
        self.BtnFantsy.clicked.connect(lambda: MainWidget.choose(0))
        self.BtnGod.clicked.connect(lambda: MainWidget.choose(2))
        self.BtnCTY.clicked.connect(lambda: MainWidget.choose(4))
        self.BtnHistory.clicked.connect(lambda: MainWidget.choose(6))
        self.BtnGame.clicked.connect(lambda: MainWidget.choose(1))
        self.BtnStrange.clicked.connect(lambda: MainWidget.choose(3))
        self.BtnComplete.clicked.connect(lambda: MainWidget.choose(5))
        self.BtnAll.clicked.connect(lambda: MainWidget.choose(7))
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "小说阅读器"))
        self.BtnFantsy.setText(_translate("MainWidget", "玄幻.奇幻小说排行榜"))
        self.BtnGod.setText(_translate("MainWidget", "修真.仙侠小说排行榜"))
        self.BtnCTY.setText(_translate("MainWidget", "都市.青春小说排行榜"))
        self.BtnHistory.setText(_translate("MainWidget", "历史.穿越小说排行榜"))
        self.BtnAll.setText(_translate("MainWidget", "全部小说排行榜"))
        self.BtnComplete.setText(_translate("MainWidget", "全本小说排行榜"))
        self.BtnStrange.setText(_translate("MainWidget", "科技.灵异小说排行榜"))
        self.BtnGame.setText(_translate("MainWidget", "网游.竞技小说排行榜"))
        self.label.setText(_translate("MainWidget", "小说阅读器"))
