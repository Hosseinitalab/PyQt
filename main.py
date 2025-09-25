# Import Modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

# Main App Object and Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Random Word Maker')
main_window.resize(300, 200)

# Create All App Objects
title = QLabel('Random Keywords')
text_1 = QLabel('?')
text_2 = QLabel('?')
text_3 = QLabel('?')

button_1 = QPushButton('Click Me')
button_2 = QPushButton('Click Me')
button_3 = QPushButton('Click Me')

# All Design Here
master_layout = QVBoxLayout()
row_1 = QHBoxLayout()
row_2 = QHBoxLayout()
row_3 = QHBoxLayout()

row_1.addWidget(title, alignment=Qt.AlignCenter)
row_2.addWidget(text_1, alignment=Qt.AlignCenter)
row_2.addWidget(text_2, alignment=Qt.AlignCenter)
row_2.addWidget(text_3, alignment=Qt.AlignCenter)
row_3.addWidget(button_1)
row_3.addWidget(button_2)
row_3.addWidget(button_3)

master_layout.addLayout(row_1)
master_layout.addLayout(row_2)
master_layout.addLayout(row_3)

# Events
main_window.setLayout(master_layout)

# Show/Run The App
main_window.show()
app.exec_()