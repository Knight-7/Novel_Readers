# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'read.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_read(object):
    def setupUi(self, read):
        read.setObjectName("read")
        read.resize(1154, 567)
        self.label_chapter = QtWidgets.QLabel(read)
        self.label_chapter.setGeometry(QtCore.QRect(460, 20, 271, 41))
        self.label_chapter.setObjectName("label_chapter")
        self.label_chapter.setStyleSheet("font: 20pt \"楷体\";\n"
"text-align:\"middle\";")
        self.textBrowser_novel_text = QtWidgets.QTextBrowser(read)
        self.textBrowser_novel_text.setGeometry(QtCore.QRect(0, 90, 1161, 481))
        self.textBrowser_novel_text.setStyleSheet("QTextBrowser { background-color: rgb(255, 132, 139, 0);\n"
"border-radius: 3px; color: rgb(0, 0, 0);\n"
"font: 18pt \"宋体\";}")
        self.textBrowser_novel_text.setObjectName("textBrowser_novel_text")
        self.pushButton_pre = QtWidgets.QPushButton(read)
        self.pushButton_pre.setGeometry(QtCore.QRect(70, 20, 151, 41))
        self.pushButton_pre.setObjectName("pushButton_pre")
        self.pushButton_next = QtWidgets.QPushButton(read)
        self.pushButton_next.setGeometry(QtCore.QRect(860, 20, 151, 41))
        self.pushButton_next.setObjectName("pushButton_next")

        self.retranslateUi(read)
        QtCore.QMetaObject.connectSlotsByName(read)

    def retranslateUi(self, read):
        _translate = QtCore.QCoreApplication.translate
        read.setWindowTitle(_translate("read", "Form"))
        self.label_chapter.setText(_translate("read", "TextLabel"))
        self.pushButton_pre.setText(_translate("read", "上一章"))
        self.pushButton_next.setText(_translate("read", "下一章"))
