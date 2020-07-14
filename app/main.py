from PyQt5.QtWidgets import QApplication
import sys
from gui.forms import MainWindow


if __name__ == '__main__':

    app = QApplication([])
    win = MainWindow()
    win.open()
    sys.exit(app.exec())
