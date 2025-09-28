# Import Modules
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout

class CalcApp(QWidget):
    def __init__(self):
        super().__init__()
        # Main App Object and Settings
        self.setWindowTitle('Calculator App')
        self.resize(250, 300)

        # Create All App Objects
        self.result = QLineEdit()
        self.grid = QGridLayout()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        self.clear = QPushButton('Clear')
        self.delete = QPushButton('<')

        row = 0
        col = 0
        for text in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            self.grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                row += 1
                col = 0
        master_layout = QVBoxLayout()
        button_row = QHBoxLayout()
        master_layout.addWidget(self.result)
        master_layout.addLayout(self.grid)
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)

        master_layout.addLayout(button_row)
        self.setLayout(master_layout)

        # Events
        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)

    def button_click(self):
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



# Show/Run The App
app = QApplication([])
main_window = CalcApp()
main_window.show()
app.exec_()
