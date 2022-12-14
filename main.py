from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, \
    QGridLayout, QStyleFactory
import sys

# TODO  extract code to separate functions, optimise for reading
class AppWindow(QMainWindow):
    calc_num_btn = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    calc_act_btn = ('+', '-', '*', '/', '%', '(', ')', '=', 'CLR')
    numbers = []
    actions = []
    total = 0
    show_expr_win = ''

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Calculator")
        self.setFixedSize(QSize(300, 560))
        # TODO extract to function 1
        # self.btn0 = QPushButton('0')
        key_layout = QGridLayout()
        self.row = 2
        self.position = 0
        for btn in self.calc_num_btn:
            tmp_name = 'btn_' + btn
            tmp_action = 'action_' + btn
            self.tmp_name = QPushButton(btn)
            self.tmp_name.setObjectName(btn)
            self.tmp_name.clicked.connect(self.parse_keyb)
            if btn == '0':
                self.position = 1
            key_layout.addWidget(self.tmp_name, self.row, self.position)
            if self.position < 2:
                self.position += 1
            else:
                self.position = 0
                self.row += 1
            if btn == '0':
                self.position = 0

        self.show_expression = QLabel()
        self.show_result = QLabel()
        key_layout.addWidget(self.show_expression, 0, 0)
        key_layout.addWidget(self.show_result, 1, 0)

        keypad = QWidget()
        keypad.setFixedSize(220, 180)
        keypad.setLayout(key_layout)
        action_layout = QGridLayout()
        action_pad = QWidget()
        action_pad.setFixedSize(220, 120)
        action_pad.setLayout(action_layout)

        for btn in self.calc_act_btn:
            tmp_name = 'btn_' + btn
            self.tmp_name = QPushButton(btn, self)
            self.tmp_name.setObjectName(btn)
            self.tmp_name.clicked.connect(self.parse_keyb)
            action_layout.addWidget(self.tmp_name, self.row, self.position)
            if self.position < 2:
                self.position += 1
            else:
                self.position = 0
                self.row += 1

        main_grid = QWidget()
        main_layout = QGridLayout()
        main_layout.addWidget(keypad)
        main_layout.addWidget(action_pad)
        main_grid.setLayout(main_layout)

        self.setCentralWidget(main_grid)
        # current value of button
        self.btn_value = ''
        # value to add to numbers list
        self.num_to_add = ''
    def parse_keyb(self):
        # get button value as string
        self.btn_value = self.sender().objectName()
        # display expression to user
        self.show_expr_win += self.btn_value
        self.show_expression.setText(self.show_expr_win)
        # CALCULATE - parse entries and put numbers and actions in dictionaries
        if self.btn_value == 'CLR':
            self.total = 0
            self.btn_value = ''
            self.num_to_add = ''
            self.show_expr_win = ''
            self.numbers.clear()
            self.actions.clear()
            self.show_expression.setText('')
            self.show_result.setText('')
        else:
            if self.btn_value == '=':
                self.numbers.append(self.num_to_add)
                self.calculate()
                self.show_expression.setText(str(self.show_expr_win))
                self.show_result.setText(str(self.total))
            elif self.btn_value in self.calc_num_btn:
                self.num_to_add += self.btn_value
                self.btn_value = ''
            else:
                # TODO if result is not empty, use result in calculations
                self.numbers.append(self.num_to_add)
                self.actions.append(self.btn_value)
                self.num_to_add = ''
                self.btn_value = ''

    # TODO extract to class
    # TODO implement actions with result and one number in numbers list
    def calculate(self):
        show_result = False
        index = None
        # create loop
        # do all multiply`s
        # do all divide`s
        # do all plus
        # do all minus
        while not show_result:
            # if use previous result
            if '*' in self.actions:
                index = self.actions.index('*')
                if int(self.numbers[index]) >= 0 and int(self.numbers[index+1]) >= 0:
                    self.total = int(self.numbers[index]) * int(self.numbers[index+1])
                    self.actions.pop(index)
                    self.numbers[index] = self.total
                    self.numbers.pop(index+1)
                else:
                    self.total = 0
            if '/' in self.actions:
                index = self.actions.index('/')
                if int(self.numbers[index]) >= 0 and int(self.numbers[index+1]) >= 0:
                    self.total = int(self.numbers[index]) / int(self.numbers[index+1])
                    self.actions.pop(index)
                    self.numbers[index] = self.total
                    self.numbers.pop(index+1)
                else:
                    self.total = 0

            if '+' in self.actions:
                index = self.actions.index('+')
                if int(self.numbers[index]) >= 0 and int(self.numbers[index+1]) >= 0:
                    self.total = int(self.numbers[index]) + int(self.numbers[index+1])
                    self.actions.pop(index)
                    self.numbers[index] = self.total
                    self.numbers.pop(index+1)
                else:
                    self.total = 0

            if '-' in self.actions:
                index = self.actions.index('-')
                if int(self.numbers[index]) >= 0 and int(self.numbers[index+1]) >= 0:
                    self.total = int(self.numbers[index]) - int(self.numbers[index+1])
                    self.actions.pop(index)
                    self.numbers[index] = self.total
                    self.numbers.pop(index+1)
                else:
                    self.total = 0

            if len(self.actions) == 0:
                show_result = True


app = QApplication(sys.argv)
app.setStyle('Fusion')
win = AppWindow()
win.show()

app.exec()
