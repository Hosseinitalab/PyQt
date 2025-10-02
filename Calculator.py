from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QFont

class CalcApp(QWidget):
    """ Calculator Class """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator App')
        self.resize(250, 300)

        # Design
        self.result = QLineEdit()
        self.result.setFont(QFont("Helvetica", 25))
        self.result.setStyleSheet("QLineEdit { background-color: green; color: white}")
        self.grid = QGridLayout()
        self.clear = QPushButton('Clear')
        self.delete = QPushButton('<')
        self.clear.setStyleSheet("QPushButton { font: 17pt Comic Sans Ms; padding: 10px; background-color: orange }")
        self.delete.setStyleSheet("QPushButton { font: 17pt Comic Sans Ms; padding: 10px; background-color: orange }")
        self.button()

        # Layout
        master_layout = QVBoxLayout()
        button_row = QHBoxLayout()
        master_layout.addWidget(self.result)
        master_layout.addLayout(self.grid)
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)
        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(25, 25, 25, 25)
        self.setLayout(master_layout)

        # Events
        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)

    def button(self):
        """ Button Creation """

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        row = 0
        col = 0
        for text in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            button.setStyleSheet("QPushButton { font: 17pt Comic Sans Ms; padding: 10px; }")
            self.grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                row += 1
                col = 0

    def button_click(self):
        """ Button Event """

        button = app.sender() # determines which button was clicked
        text = button.text()
        
        match text:
            case '=':
                symbol = self.result.text()
                try:
                    res = eval(symbol)
                    self.result.setText(str(res))
                except Exception as e:
                    print('Error: ', e)
            case 'Clear':
                self.result.clear()
            case '<':
                current_value = self.result.text()
                self.result.setText(current_value[:-1])
            case _:
                current_value = self.result.text()
                self.result.setText(current_value + text)

if __name__ == '__main__':
    app = QApplication([])
    main_window = CalcApp()
    main_window.setStyleSheet("QWidget {background-color: white}")
    main_window.show()
    app.exec_()
