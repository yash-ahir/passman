# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 506)
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.togglePassword = QtWidgets.QToolButton(self.groupBox)
        self.togglePassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.togglePassword.setText("")
        self.togglePassword.setIconSize(QtCore.QSize(16, 16))
        self.togglePassword.setCheckable(True)
        self.togglePassword.setObjectName("togglePassword")
        self.gridLayout_2.addWidget(self.togglePassword, 2, 3, 1, 1)
        self.passwordField = QtWidgets.QLineEdit(self.groupBox)
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordField.setReadOnly(True)
        self.passwordField.setObjectName("passwordField")
        self.gridLayout_2.addWidget(self.passwordField, 2, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.copyPassword = QtWidgets.QToolButton(self.groupBox)
        self.copyPassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.copyPassword.setText("")
        self.copyPassword.setObjectName("copyPassword")
        self.gridLayout_2.addWidget(self.copyPassword, 2, 4, 1, 1)
        self.titleField = QtWidgets.QLineEdit(self.groupBox)
        self.titleField.setReadOnly(True)
        self.titleField.setObjectName("titleField")
        self.gridLayout_2.addWidget(self.titleField, 0, 1, 1, 4)
        self.accountField = QtWidgets.QLineEdit(self.groupBox)
        self.accountField.setReadOnly(True)
        self.accountField.setObjectName("accountField")
        self.gridLayout_2.addWidget(self.accountField, 1, 1, 1, 4)
        self.noteField = QtWidgets.QTextEdit(self.groupBox)
        self.noteField.setReadOnly(True)
        self.noteField.setObjectName("noteField")
        self.gridLayout_2.addWidget(self.noteField, 4, 1, 1, 4)
        self.editButton = QtWidgets.QPushButton(self.groupBox)
        self.editButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editButton.setObjectName("editButton")
        self.gridLayout_2.addWidget(self.editButton, 5, 1, 1, 1)
        self.removeButton = QtWidgets.QPushButton(self.groupBox)
        self.removeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.removeButton.setObjectName("removeButton")
        self.gridLayout_2.addWidget(self.removeButton, 5, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        self.newButton = QtWidgets.QPushButton(self.centralwidget)
        self.newButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.newButton.setObjectName("newButton")
        self.gridLayout.addWidget(self.newButton, 1, 1, 1, 1)
        self.listEntries = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listEntries.sizePolicy().hasHeightForWidth())
        self.listEntries.setSizePolicy(sizePolicy)
        self.listEntries.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listEntries.setObjectName("listEntries")
        self.gridLayout.addWidget(self.listEntries, 0, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 642, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.listEntries, self.titleField)
        MainWindow.setTabOrder(self.titleField, self.accountField)
        MainWindow.setTabOrder(self.accountField, self.passwordField)
        MainWindow.setTabOrder(self.passwordField, self.togglePassword)
        MainWindow.setTabOrder(self.togglePassword, self.copyPassword)
        MainWindow.setTabOrder(self.copyPassword, self.noteField)
        MainWindow.setTabOrder(self.noteField, self.editButton)
        MainWindow.setTabOrder(self.editButton, self.removeButton)
        MainWindow.setTabOrder(self.removeButton, self.newButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PassMan - Entries"))
        self.label_4.setText(_translate("MainWindow", "Title:"))
        self.label_2.setText(_translate("MainWindow", "Password:"))
        self.togglePassword.setToolTip(_translate("MainWindow", "Toggle Password Visibility"))
        self.label_3.setText(_translate("MainWindow", "Note:"))
        self.label.setText(_translate("MainWindow", "Account:"))
        self.copyPassword.setToolTip(_translate("MainWindow", "Copy Password To Clipboard"))
        self.editButton.setText(_translate("MainWindow", "Edit"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.newButton.setText(_translate("MainWindow", "New Entry"))
