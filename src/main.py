import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from MainWindow import Ui_MainWindow
from setmasterDialog import Ui_setmasterDialog
from passwordDialog import Ui_passwordDialog
from loginDialog import Ui_loginDialog
from deleteDialog import Ui_deleteDialog
from dbQueries import *
from randomPass import generatePass
from bson import ObjectId
import pyperclip

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.key = ""
        self.listEntries.setFocus()
        self.login()
        self.togglePassword.pressed.connect(lambda: toggleEcho(self.togglePassword.isChecked(), self.togglePassword, self.passwordField))
        self.loadEntries()
        self.listEntries.itemClicked.connect(self.displayEntry)
        self.newButton.pressed.connect(self.newEntry)
        self.removeButton.pressed.connect(self.deleteEntry)
        self.editButton.pressed.connect(self.editEntry)
        self.copyPassword.pressed.connect(lambda: copyPass(self.passwordField))
        self.togglePassword.setIcon(QIcon("icons/lock.svg"))
        self.editButton.setIcon(QIcon("icons/edit.svg"))
        self.removeButton.setIcon(QIcon("icons/minus.svg"))
        self.newButton.setIcon(QIcon("icons/plus.svg"))
        self.copyPassword.setIcon(QIcon("icons/clipboard.svg"))
        self.setWindowIcon(QIcon("icons/shield.svg"))

    def login(self):
        if not checkMasterkey():
            dialog = setmasterDialog()
            dialog.show()
            dialog.exec_()
            if not checkMasterkey():
                sys.exit()
            self.key = dialog.key
        else:
            dialog = loginDialog()
            dialog.show()
            dialog.exec_()
            if not dialog.status:
                sys.exit()
            self.key = dialog.key

    def loadEntries(self):
        entries = getAll()
        self.listEntries.clear()
        self.clearData()
        for entry in entries:
            item = QListWidgetItem(self.listEntries)
            item.setData(Qt.DisplayRole, entry["title"])
            item.setData(Qt.UserRole, str(entry["_id"]))
            self.listEntries.addItem(item)

    def newEntry(self):
        self.setDisabled(True)
        dialog = passwordDialog(self.key)
        dialog.show()
        dialog.exec_()
        self.loadEntries()
        self.setDisabled(False)
        self.groupBox.setEnabled(False)

    def displayEntry(self, entry):
        self.groupBox.setEnabled(True)
        self.clearData()
        entryId = ObjectId(entry.data(Qt.UserRole))
        self.titleField.setText(getTitle(entryId))
        self.accountField.setText(getAccount(entryId))
        self.passwordField.setText(getPassword(entryId, self.key))
        self.noteField.setText(getNote(entryId))

    def clearData(self):
        self.titleField.clear()
        self.accountField.clear()
        self.passwordField.clear()
        self.noteField.clear()
        toggleEcho(True, self.togglePassword, self.passwordField)
        self.togglePassword.setChecked(False)

    def deleteEntry(self):
        self.setDisabled(True)
        entryId = self.listEntries.currentItem().data(Qt.UserRole)
        dialog = deleteDialog(entryId)
        dialog.show()
        dialog.exec_()
        if dialog.status:
            removeEntry(ObjectId(entryId))
        self.loadEntries()
        self.setDisabled(False)
        self.groupBox.setEnabled(False)

    def editEntry(self):
        self.setDisabled(True)
        dialog = editDialog(self.key, ObjectId(self.listEntries.currentItem().data(Qt.UserRole)))
        dialog.show()
        dialog.exec_()
        self.loadEntries()
        self.setDisabled(False)
        self.groupBox.setEnabled(False)

class passwordDialog(QDialog, Ui_passwordDialog):
    def __init__(self, key):
        super(passwordDialog, self).__init__()
        self.setupUi(self)
        self.key = key
        self.titleField.setFocus()
        self.dialogButtons.button(QDialogButtonBox.Ok).setDisabled(True)
        self.titleField.textChanged.connect(self.checkFilled)
        self.accountField.textChanged.connect(self.checkFilled)
        self.passwordField.textChanged.connect(self.checkFilled)
        self.dialogButtons.button(QDialogButtonBox.Ok).pressed.connect(self.addEntry)
        self.togglePassword.pressed.connect(lambda: toggleEcho(self.togglePassword.isChecked(), self.togglePassword, self.passwordField))
        self.generateRandom.pressed.connect(self.genPass)
        self.copyPassword.pressed.connect(lambda: copyPass(self.passwordField))
        self.togglePassword.setIcon(QIcon("icons/lock.svg"))
        self.copyPassword.setIcon(QIcon("icons/clipboard.svg"))
        self.setWindowIcon(QIcon("icons/shield.svg"))

    def addEntry(self):
        title = self.titleField.text()
        account = self.accountField.text()
        password = self.passwordField.text()
        note = self.noteField.toPlainText()
        addEntry(self.key, title, account, password, note)

    def genPass(self):
        password = generatePass(int(self.passwordLength.text()))
        self.passwordField.setText(password)

    def checkFilled(self):
        if (self.titleField.text() != "") and (self.accountField.text() != "") and (self.passwordField.text() != ""):
            self.dialogButtons.button(QDialogButtonBox.Ok).setDisabled(False)
        else:
            self.dialogButtons.button(QDialogButtonBox.Ok).setDisabled(True)

class setmasterDialog(QDialog, Ui_setmasterDialog):
    def __init__(self):
        super(setmasterDialog, self).__init__()
        self.setupUi(self)
        self.dialogButtons.button(QDialogButtonBox.Ok).setDisabled(True)
        self.masterkeyField.textChanged.connect(self.checkFilled)
        self.confirmField.textChanged.connect(self.checkFilled)
        self.dialogButtons.button(QDialogButtonBox.Cancel).pressed.connect(self.exit)
        self.toggleMasterkey.pressed.connect(lambda: toggleEcho(self.toggleMasterkey.isChecked(), self.toggleMasterkey, self.masterkeyField))
        self.toggleConfirm.pressed.connect(lambda: toggleEcho(self.toggleConfirm.isChecked(), self.toggleConfirm, self.confirmField))
        self.dialogButtons.button(QDialogButtonBox.Ok).pressed.connect(self.setMaster)
        self.key = ""
        self.toggleMasterkey.setIcon(QIcon("icons/lock.svg"))
        self.toggleConfirm.setIcon(QIcon("icons/lock.svg"))
        self.setWindowIcon(QIcon("icons/shield.svg"))

    def setMaster(self):
        setMasterkey(self.masterkeyField.text())
        self.key = self.masterkeyField.text()

    def checkFilled(self):
        if (self.masterkeyField.text() != "") and (self.confirmField.text() != "") and (self.masterkeyField.text() == self.confirmField.text()) and (len(self.masterkeyField.text()) >= 8):
            self.dialogButtons.button(QDialogButtonBox.Ok).setDisabled(False)
        else:
            self.dialogButtons.button(QDialogButtonBox.Ok).setDisabled(True)

    def exit(self):
        sys.exit()

class loginDialog(QDialog, Ui_loginDialog):
    def __init__(self):
        super(loginDialog, self).__init__()
        self.setupUi(self)
        self.dialogButtons.button(QDialogButtonBox.Ok).setDisabled(True)
        self.masterkeyField.textChanged.connect(self.checkFilled)
        self.status = False
        self.toggleMasterkey.pressed.connect(lambda: toggleEcho(self.toggleMasterkey.isChecked(), self.toggleMasterkey, self.masterkeyField))
        self.key = ""
        self.dialogButtons.button(QDialogButtonBox.Ok).pressed.connect(self.authenticate)
        self.toggleMasterkey.setIcon(QIcon("icons/lock.svg"))
        self.setWindowIcon(QIcon("icons/shield.svg"))

    def checkFilled(self):
        if self.masterkeyField.text() != "":
            self.dialogButtons.button(QDialogButtonBox.Ok).setDisabled(False)
        else:
            self.dialogButtons.button(QDialogButtonBox.Ok).setDisabled(True)

    def authenticate(self):
        masterKey, salt = getMasterkey()
        hashedKey = hashKey(self.masterkeyField.text(), bytes.fromhex(salt)).hex()
        if hashedKey == masterKey:
            self.status = True
            self.key = self.masterkeyField.text()

class editDialog(passwordDialog):
    def __init__(self, key, entryId):
        super().__init__(key)
        self.key = key
        self.entryId = entryId
        self.setWindowTitle("PassMan - Edit entry")
        self.titleField.setText(getTitle(entryId))
        self.accountField.setText(getAccount(entryId))
        self.passwordField.setText(getPassword(entryId, key))
        self.noteField.setText(getNote(entryId))
    
    def addEntry(self):
        editEntry(self.entryId, self.key, self.titleField.text(), self.accountField.text(), self.passwordField.text(), self.noteField.toPlainText())

class deleteDialog(QDialog, Ui_deleteDialog):
    def __init__(self, entryId):
        super(deleteDialog, self).__init__()
        self.setupUi(self)
        self.status = False
        title = getTitle(ObjectId(entryId))
        self.warningLabel.setText(f"Delete entry {title}? You won't be able to recover it!")
        self.dialogButtons.setStandardButtons(QDialogButtonBox.No | QDialogButtonBox.Yes)
        self.dialogButtons.button(QDialogButtonBox.Yes).pressed.connect(self.confirmDelete)
        self.setWindowIcon(QIcon("icons/shield.svg"))
    
    def confirmDelete(self):
        self.status = True

def toggleEcho(status, button, field):
    if status:
        field.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        button.setIcon(QIcon("icons/lock.svg"))
    else:
        field.setEchoMode(QLineEdit.Normal)
        button.setIcon(QIcon("icons/unlock.svg"))

def copyPass(field):
    pyperclip.copy(field.text())

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()