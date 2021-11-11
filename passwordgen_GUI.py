# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passwordgenUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PasswordGenerator(object):
    def setupUi(self, PasswordGenerator):
        PasswordGenerator.setObjectName("PasswordGenerator")
        PasswordGenerator.resize(240, 320)
        PasswordGenerator.setMinimumSize(QtCore.QSize(240, 320))
        PasswordGenerator.setMaximumSize(QtCore.QSize(240, 320))
        self.numberofpasswords = QtWidgets.QTextEdit(PasswordGenerator)
        self.numberofpasswords.setGeometry(QtCore.QRect(190, 20, 31, 21))
        self.numberofpasswords.setObjectName("numberofpasswords")
        self.numberofletters = QtWidgets.QTextEdit(PasswordGenerator)
        self.numberofletters.setGeometry(QtCore.QRect(190, 50, 31, 21))
        self.numberofletters.setObjectName("numberofletters")
        self.numberofnumbers = QtWidgets.QTextEdit(PasswordGenerator)
        self.numberofnumbers.setGeometry(QtCore.QRect(190, 80, 31, 21))
        self.numberofnumbers.setObjectName("numberofnumbers")
        self.numberofspecialchar = QtWidgets.QTextEdit(PasswordGenerator)
        self.numberofspecialchar.setGeometry(QtCore.QRect(190, 110, 31, 21))
        self.numberofspecialchar.setObjectName("numberofspecialchar")
        self.passwordlist = QtWidgets.QTextEdit(PasswordGenerator)
        self.passwordlist.setGeometry(QtCore.QRect(30, 140, 181, 121))
        self.passwordlist.setObjectName("passwordlist")
        self.start = QtWidgets.QPushButton(PasswordGenerator)
        self.start.setGeometry(QtCore.QRect(20, 271, 101, 41))
        self.start.setObjectName("start")
        self.save = QtWidgets.QPushButton(PasswordGenerator)
        self.save.setGeometry(QtCore.QRect(120, 270, 101, 41))
        self.save.setObjectName("save")
        self.label = QtWidgets.QLabel(PasswordGenerator)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(PasswordGenerator)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 141, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(PasswordGenerator)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 141, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(PasswordGenerator)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 161, 21))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(PasswordGenerator)
        QtCore.QMetaObject.connectSlotsByName(PasswordGenerator)

    def retranslateUi(self, PasswordGenerator):
        _translate = QtCore.QCoreApplication.translate
        PasswordGenerator.setWindowTitle(_translate("PasswordGenerator", "Password Generator"))
        self.start.setText(_translate("PasswordGenerator", "Start"))
        self.save.setText(_translate("PasswordGenerator", "Save List"))
        self.label.setText(_translate("PasswordGenerator", "Number of Passwords:"))
        self.label_2.setText(_translate("PasswordGenerator", "Number of Letters:"))
        self.label_3.setText(_translate("PasswordGenerator", "Number of Numbers:"))
        self.label_4.setText(_translate("PasswordGenerator", "Number of Special Chars:"))

