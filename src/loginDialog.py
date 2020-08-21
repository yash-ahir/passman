# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginDialog(object):
    def setupUi(self, loginDialog):
        loginDialog.setObjectName("loginDialog")
        loginDialog.resize(400, 139)
        self.gridLayout = QtWidgets.QGridLayout(loginDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.toggleMasterkey = QtWidgets.QToolButton(loginDialog)
        self.toggleMasterkey.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toggleMasterkey.setText("")
        self.toggleMasterkey.setCheckable(True)
        self.toggleMasterkey.setObjectName("toggleMasterkey")
        self.gridLayout.addWidget(self.toggleMasterkey, 1, 2, 1, 1)
        self.dialogButtons = QtWidgets.QDialogButtonBox(loginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialogButtons.sizePolicy().hasHeightForWidth())
        self.dialogButtons.setSizePolicy(sizePolicy)
        self.dialogButtons.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dialogButtons.setOrientation(QtCore.Qt.Horizontal)
        self.dialogButtons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialogButtons.setObjectName("dialogButtons")
        self.gridLayout.addWidget(self.dialogButtons, 3, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(loginDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.masterkeyField = QtWidgets.QLineEdit(loginDialog)
        self.masterkeyField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.masterkeyField.setClearButtonEnabled(True)
        self.masterkeyField.setObjectName("masterkeyField")
        self.gridLayout.addWidget(self.masterkeyField, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(loginDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.passwordMessage = QtWidgets.QLabel(loginDialog)
        self.passwordMessage.setEnabled(True)
        self.passwordMessage.setObjectName("passwordMessage")
        self.gridLayout.addWidget(self.passwordMessage, 2, 0, 1, 3)

        self.retranslateUi(loginDialog)
        self.dialogButtons.accepted.connect(loginDialog.accept)
        self.dialogButtons.rejected.connect(loginDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(loginDialog)
        loginDialog.setTabOrder(self.masterkeyField, self.toggleMasterkey)

    def retranslateUi(self, loginDialog):
        _translate = QtCore.QCoreApplication.translate
        loginDialog.setWindowTitle(_translate("loginDialog", "PassMan - Login"))
        self.toggleMasterkey.setToolTip(_translate("loginDialog", "Toggle password visibility"))
        self.label_2.setText(_translate("loginDialog", "Master key:"))
        self.masterkeyField.setToolTip(_translate("loginDialog", "Enter your master key/password"))
        self.masterkeyField.setPlaceholderText(_translate("loginDialog", "Enter your master key/password"))
        self.label.setText(_translate("loginDialog", "Welcome to PassMan!"))
        self.passwordMessage.setText(_translate("loginDialog", "Wrong password, please try again."))
