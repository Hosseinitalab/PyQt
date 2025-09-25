# Import Modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

# Main App Object and Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Random Word Maker')
main_window.resize(300, 200)

# Create All App Objects

# All Design Here

# Events

# Show/Run The App
main_window.show()
app.exec_()