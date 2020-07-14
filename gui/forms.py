from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self._ui = loadUi('MainWindow.ui')
        self._ui.sendButton.clicked.connect(self.send_message)
        self._ui.clearButton.clicked.connect(self.clear_fields)
        self._ui.groupButton.clicked.connect(self.add_group)
        self._ui.emailButton.clicked.connect(self.add_email)

    def open(self):
        self._ui.show()

    def send_message(self):
        QMessageBox.information(self, 'Test', 'send_message-OK')

    def clear_fields(self):
        QMessageBox.information(self, 'Test', 'clear_fields-OK')

    def add_group(self):
        QMessageBox.information(self, 'Test', 'add_group-OK')

    def add_email(self):
        QMessageBox.information(self, 'Test', 'add_email-OK')
