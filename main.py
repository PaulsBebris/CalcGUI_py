from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, \
    QGridLayout, QStyleFactory
import sys


class AppWindow(QMainWindow):
    calc_btn = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '%', '(', ')', '=')
    numbers = {}
    actions = {}
    total = 0

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Calculator")
        self.setFixedSize(QSize(300, 560))
        # TODO extract to function 1
        # self.btn0 = QPushButton('0')
        key_layout = QGridLayout()
        self.row = 0
        self.position = 0
        for btn in self.calc_btn:
            tmp_name = 'btn_' + btn
            self.tmp_name = QPushButton(btn)
            key_layout.addWidget(self.tmp_name, self.row, self.position)
            if self.position < 2:
                self.position += 1
            else:
                self.position = 0
                self.row += 1

        keypad = QWidget()
        keypad.setFixedSize(150, 150)
        keypad.setLayout(key_layout)

        main_grid = QWidget()
        main_layout = QGridLayout()
        main_layout.addWidget(keypad)
        main_grid.setLayout(main_layout)

        self.setCentralWidget(main_grid)

    # def plus(self):
    #     self.actions.append('+')
    #
    # def minus(self):
    #     self.actions.append('-')
    #
    # def multiply(self):
    #     self.actions.append('*')
    #
    # def divide(self):
    #     self.actions.append('/')
    #
    # def calculate(self):
    #    self.parseInput()


app = QApplication(sys.argv)
app.setStyle('Fusion')
win = AppWindow()
win.show()

app.exec()
