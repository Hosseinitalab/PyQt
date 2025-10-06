# Import Modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from random import choice

# Main App Object and Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Random Word Maker')
main_window.resize(300, 200)

# Create All App Objects
title = QLabel('Random Keywords')
text_1 = QLabel('?')
text_2 = QLabel('?')

button_1 = QPushButton('Click Me')
button_2 = QPushButton('Eraser')

word_list = ['Behzad', 'Mohammad Reza', 'Ahmad Reaz', 'Zahra', 'Mobina', 'Farzaneh', 'Negar', 'Reza', 'Paria']

# All Design Here
master_layout = QVBoxLayout()
row_1 = QHBoxLayout()
row_2 = QHBoxLayout()
row_3 = QHBoxLayout()

row_1.addWidget(title, alignment=Qt.AlignCenter)
row_2.addWidget(text_1, alignment=Qt.AlignCenter)
row_2.addWidget(text_2, alignment=Qt.AlignCenter)
row_3.addWidget(button_1)
row_3.addWidget(button_2)

master_layout.addLayout(row_1)
master_layout.addLayout(row_2)
master_layout.addLayout(row_3)

main_window.setLayout(master_layout)

# Create Functions
def random_word():
    text_1.setText(choice(word_list))
    text_2.setText(choice(word_list))
def eraser():
    text_1.setText('?')
    text_2.setText('?')

# Events
button_1.clicked.connect(random_word)
button_2.clicked.connect(eraser)

# Show/Run The App
main_window.show()
app.exec_()