from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QListWidget, QComboBox
from PIL import Image, ImageFilter, ImageEnhance
import os


class PhotoEdit(QWidget):
    def __init__(self):
        self.app = QApplication([])
        super().__init__()
        self.setWindowTitle("Photo Editer")
        self.resize(900, 700)

        self.__design()
        self.__layout()

    def __design(self):
        # folder list
        self.file_list = QListWidget()
        self.folder_button = QPushButton("Folder")
        self.folder_button.clicked.connect(self.gathering_files)
        self.file_list.currentRowChanged.connect(self.__load_image)

        # filters
        self.left_button = QPushButton("Left")
        self.right_button = QPushButton("Right")
        self.mirror_button = QPushButton("Mirror")
        self.sharpness_button = QPushButton("Sharpness")
        self.gray_button = QPushButton("Gray")
        self.saturation_button = QPushButton("Saturation")
        self.contrast_button = QPushButton("Contrast")
        self.blur_button = QPushButton("Blur")

        # combo box
        self.filter_box = QComboBox()
        self.filter_box.addItem("Original")
        self.filter_box.addItem("Left")
        self.filter_box.addItem("Right")
        self.filter_box.addItem("Mirror")
        self.filter_box.addItem("Sharpness")
        self.filter_box.addItem("Gray")
        self.filter_box.addItem("Color")
        self.filter_box.addItem("Contrast")
        self.filter_box.addItem("Blur")

        # picture box
        self.picture_box = QLabel("Image will appear here!")

    def __layout(self):
        master_layout = QHBoxLayout()
        col_1 = QVBoxLayout()
        col_2 = QVBoxLayout()

        col_1.addWidget(self.folder_button)
        col_1.addWidget(self.file_list)
        col_1.addWidget(self.filter_box)
        col_1.addWidget(self.left_button)
        col_1.addWidget(self.right_button)
        col_1.addWidget(self.mirror_button)
        col_1.addWidget(self.sharpness_button)
        col_1.addWidget(self.gray_button)
        col_1.addWidget(self.saturation_button)
        col_1.addWidget(self.contrast_button)
        col_1.addWidget(self.blur_button)
        col_2.addWidget(self.picture_box)

        master_layout.addLayout(col_1, 20)
        master_layout.addLayout(col_2, 80)
        self.setLayout(master_layout)

    def search_photo(self, file):
        for ext in self.extensions:
            if file.endswith(ext):
                return file
    
    def gathering_files(self):
        self.working_directory = os.getcwd()
        self.extensions = ('.jpg', '.jpeg', 'png', '.svg')
        file_names = list(filter(self.search_photo, os.listdir(self.working_directory)))
        self.file_list.clear()
        for file in file_names:
            self.file_list.addItem(file)

    def __select_image(self):
        if self.file_list.currentRow() >= 0:
            return self.file_list.currentItem().text()
        else:
            return None
        
    def __load_image(self):
        file_name = self.__select_image()
        if file_name != None:
            self.full_name = os.path.join(self.working_directory, file_name)
            self.image = Image.open(self.full_name)
            self.original_image = self.image.copy()
            self.__show_image()
   
    def __show_image(self):
        self.picture_box.hide()
        image = QPixmap(self.full_name)
        w, h = self.picture_box.width(), self.picture_box.height()
        image = image.scaled(w, h, Qt.KeepAspectRatio)
        self.picture_box.setPixmap(image)
        self.picture_box.show()
    
    def save_image(self):
        pass

    def _run(self):
        self.show()
        self.app.exec_()

program = PhotoEdit()
program._run()
