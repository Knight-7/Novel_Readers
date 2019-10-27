# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(502, 661)
        self.label_list_name = QtWidgets.QLabel(Widget)
        self.label_list_name.setGeometry(QtCore.QRect(10, 20, 461, 31))
        self.label_list_name.setStyleSheet("font: 20pt \"楷体\";\n"
"text-align:\"middle\";")
        self.label_list_name.setObjectName("label_list_name")
        self.verticalLayoutWidget = QtWidgets.QWidget(Widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 90, 141, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_picture = QtWidgets.QLabel(Widget)
        self.label_picture.setGeometry(QtCore.QRect(170, 70, 141, 211))
        self.label_picture.setObjectName("label_picture")
        self.label_author = QtWidgets.QLabel(Widget)
        self.label_author.setGeometry(QtCore.QRect(340, 120, 181, 31))
        self.label_author.setObjectName("label_author")
        self.label_title = QtWidgets.QLabel(Widget)
        self.label_title.setGeometry(QtCore.QRect(330, 60, 161, 61))
        self.label_title.setStyleSheet("font: 20pt \"楷体\";")
        self.label_title.setObjectName("label_title")
        self.jianjie = QtWidgets.QTextBrowser(Widget)
        self.jianjie.setGeometry(QtCore.QRect(330, 170, 161, 111))
        self.jianjie.setStyleSheet("QTextEdit { background-color: rgb(255, 132, 139, 0);\n"
"border-radius: 3px; color: rgb(0, 0, 0);}")
        self.jianjie.setObjectName("jianjie")
        self.gridLayoutWidget = QtWidgets.QWidget(Widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(170, 320, 321, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_pre_page = QtWidgets.QPushButton(Widget)
        self.pushButton_pre_page.setGeometry(QtCore.QRect(170, 590, 93, 28))
        self.pushButton_pre_page.setObjectName("pushButton_pre_page")
        self.pushButton_next_page = QtWidgets.QPushButton(Widget)
        self.pushButton_next_page.setGeometry(QtCore.QRect(390, 590, 93, 28))
        self.pushButton_next_page.setObjectName("pushButton_next_page")
        self.lineEdit_page = QtWidgets.QLineEdit(Widget)
        self.lineEdit_page.setGeometry(QtCore.QRect(280, 590, 41, 21))
        self.lineEdit_page.setObjectName("lineEdit_page")
        self.label_total_page = QtWidgets.QLabel(Widget)
        self.label_total_page.setGeometry(QtCore.QRect(330, 585, 41, 31))
        self.label_total_page.setObjectName("label_total_page")
        self.pushButton_quit = QtWidgets.QPushButton(Widget)
        self.pushButton_quit.setGeometry(QtCore.QRect(392, 630, 111, 31))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 141, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_total = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_total.setObjectName("pushButton_total")
        self.horizontalLayout.addWidget(self.pushButton_total)
        self.pushButton_week = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_week.setObjectName("pushButton_week")
        self.horizontalLayout.addWidget(self.pushButton_week)
        self.pushButton_month = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_month.setObjectName("pushButton_month")
        self.horizontalLayout.addWidget(self.pushButton_month)
        self.pushButton_day = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_day.setObjectName("pushButton_day")
        self.horizontalLayout.addWidget(self.pushButton_day)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label_list_name.setText(_translate("Widget", "TextLabel"))
        self.label_picture.setText(_translate("Widget", "tu"))
        self.label_author.setText(_translate("Widget", "TextLabel"))
        self.label_title.setText(_translate("Widget", "TextLabel"))
        self.pushButton_pre_page.setText(_translate("Widget", "上一页"))
        self.pushButton_next_page.setText(_translate("Widget", "下一页"))
        self.label_total_page.setText(_translate("Widget", "/100"))
        self.pushButton_quit.setText(_translate("Widget", "返回主界面"))
        self.pushButton_total.setText(_translate("Widget", "总"))
        self.pushButton_week.setText(_translate("Widget", "周"))
        self.pushButton_month.setText(_translate("Widget", "月"))
        self.pushButton_day.setText(_translate("Widget", "日"))
