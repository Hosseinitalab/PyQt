# Import Modules
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout

# Main App Object and Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Calculator App')
main_window.resize(250, 300)

# Create All App Objects
result = QLineEdit()
grid = QGridLayout()
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]
clear = QPushButton('Clear')
delete = QPushButton('<')

# create Functions
def button_click():
    button = app.sender() # determines which button was clicked
    text = button.text()
    
    match text:
        case '=':
            symbol = result.text()
            try:
                res = eval(symbol)
                result.setText(str(res))
            except Exception as e:
                print('Error: ', e)
        case 'Clear':
            result.clear()
        case '<':
            current_value = result.text()
            result.setText(current_value[:-1])
        case _:
            current_value = result.text()
            result.setText(current_value + text)

# The rest of the create object
row = 0
col = 0
for text in buttons:
    button = QPushButton(text)
    button.clicked.connect(button_click)
    grid.addWidget(button, row, col)
    col += 1
    if col > 3:
        row += 1
        col = 0

# All Design Here
master_layout = QVBoxLayout()
button_row = QHBoxLayout()
master_layout.addWidget(result)
master_layout.addLayout(grid)
button_row.addWidget(clear)
button_row.addWidget(delete)

master_layout.addLayout(button_row)
main_window.setLayout(master_layout)

# Events
clear.clicked.connect(button_click)
delete.clicked.connect(button_click)

# Show/Run The App
main_window.show()
app.exec_()
