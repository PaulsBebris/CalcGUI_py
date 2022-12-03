from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
import sys


class AppWin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Booooooo")
        self.setFixedSize(QSize(300, 350))
        plus_btn = QPushButton("+")
        plus_btn.setCheckable(True)
        plus_btn.clicked.connect(self.plus)
        self.setCentralWidget(plus_btn)

    def plus(self):
        print("PLUS action")


app = QApplication(sys.argv)

win = AppWin()
win.show()

app.exec()

