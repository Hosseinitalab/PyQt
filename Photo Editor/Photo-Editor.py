from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QListWidget, QComboBox
from PIL import Image, ImageFilter, ImageEnhance
import os

class Editor:

    def __init__(self):
        pass

    def _gray(self):
        if self._image != None:
            self._image = self._image.convert('L')
            self.__confirm()

    def _mirror(self):
        if self._image != None:
            self._image = self._image.transpose(Image.FLIP_LEFT_RIGHT)
            self.__confirm()

    def _left(self):
        if self._image != None:
            self._image = self._image.transpose(Image.ROTATE_90)
            self.__confirm()

    def _right(self):
        if self._image != None:
            self._image = self._image.transpose(Image.ROTATE_270)
            self.__confirm()

    def _contrast(self):
        if self._image != None:
            self._image = ImageEnhance.Contrast(self._image).enhance(1.2)
            self.__confirm()

    def _blur(self):
        if self._image != None:
            self._image = self._image.filter(ImageFilter.BLUR)
            self.__confirm()

    def _sharpness(self):
        if self._image != None:
            self._image = self._image.filter(ImageFilter.SHARPEN)
            self.__confirm()

    def _color(self):
        if self._image != None:
            self._image = ImageEnhance.Color(self._image).enhance(1.2)
            self.__confirm()

    def __confirm(self):
            self._save_image()
            path = os.path.join(self._working_directory, self._save_folder, 'edited_' + self._file_name)
            self._show_image(path)

class GUI(QWidget, Editor):

    def __init__(self):
        Editor.__init__(self)
        self.app = QApplication([])
        super().__init__()
        self.setWindowTitle("Photo Editer")
        self.resize(900, 700)
        self._image = None
        self._save_folder = 'Edited-Photos'
        self.__design()
        self.__layout()

    def __design(self):
        # folder list
        self.file_list = QListWidget()
        self.folder_button = QPushButton("Folder")
        self.folder_button.clicked.connect(self.__gathering_files)
        self.file_list.currentRowChanged.connect(self.__load_image)

        # filters
        self.left_button = QPushButton("Left")
        self.left_button.clicked.connect(self._left)

        self.right_button = QPushButton("Right")
        self.right_button.clicked.connect(self._right)

        self.mirror_button = QPushButton("Mirror")
        self.mirror_button.clicked.connect(self._mirror)

        self.sharpness_button = QPushButton("Sharpness")
        self.sharpness_button.clicked.connect(self._sharpness)

        self.gray_button = QPushButton("Gray")
        self.gray_button.clicked.connect(self._gray)

        self.saturation_button = QPushButton("Saturation")
        self.saturation_button.clicked.connect(self._color)

        self.contrast_button = QPushButton("Contrast")
        self.contrast_button.clicked.connect(self._contrast)

        self.blur_button = QPushButton("Blur")
        self.blur_button.clicked.connect(self._blur)

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
        self.picture_box = QLabel()

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

    def __search_photo(self, file):
        for ext in self._extensions:
            if file.endswith(ext):
                return file
    
    def __gathering_files(self):
        self._working_directory = os.getcwd()
        self._extensions = ('.jpg', '.jpeg', 'png', '.svg')
        file_names = list(filter(self.__search_photo, os.listdir(self._working_directory)))
        self.file_list.clear()
        for file in file_names:
            self.file_list.addItem(file)

    def __load_image(self):
        self._file_name = self.__select_image()
        if self._file_name != None:
            self.full_name = os.path.join(self._working_directory, self._file_name)
            self._image = Image.open(self.full_name)
            self._original_image = self._image.copy()
            self._show_image(self.full_name)

    def __select_image(self):
        if self.file_list.currentRow() >= 0:
            return self.file_list.currentItem().text()
        else:
            return None
        
    def _show_image(self, path):
        self.picture_box.hide()
        image = QPixmap(path)
        w, h = self.picture_box.width(), self.picture_box.height()
        image = image.scaled(w, h, Qt.KeepAspectRatio)
        self.picture_box.setPixmap(image)
        self.picture_box.show()
    
    def _save_image(self):

        saved_working_directory = os.path.join(self._working_directory, self._save_folder)
        if not (os.path.exists(saved_working_directory) and os.path.isdir(saved_working_directory)):
            os.mkdir(saved_working_directory)
        saved_image_name = os.path.join(self._working_directory, self._save_folder, 'edited_' + self._file_name)
        self._image.save(saved_image_name)

    def _run(self):
        self.show()
        self.app.exec_()

program = GUI()
program._run()
