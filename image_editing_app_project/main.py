from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget,
                             QLabel, QPushButton, QListWidget,
                             QComboBox, QVBoxLayout, QHBoxLayout,
                             QFileDialog
)
from PIL import (Image, ImageFilter, ImageEnhance)
import sys
import os

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Editing App")
        self.resize(900, 700)
        self.editor = Editor(self)

        # --- Widgets ---
        # Image display area
        self.image_zone = QLabel("Image will appear here")

        # Folder selection
        self.select_folder_button = QPushButton("Select folder")
        self.select_folder_button.clicked.connect(self.get_work_directory)

        # List of objects (images)
        self.file_list = QListWidget()
        self.file_list.currentRowChanged.connect(self.display_image)

        # Function selection dropdown
        self.function_select_box = QComboBox()
        self.function_select_box.addItems([
            "Original", "Left", "Right", "Mirror",
            "Sharpness", "B/W", "Colour", "Contrast"
        ])

        # Function buttons
        self.left_button = QPushButton("Left")
        self.left_button.clicked.connect(self.editor.left)
        self.right_button = QPushButton("Right")
        self.right_button.clicked.connect(self.editor.right)
        self.mirror_button = QPushButton("Mirror")
        self.mirror_button.clicked.connect(self.editor.mirror)
        self.sharpness_button = QPushButton("Sharpness")
        self.sharpness_button.clicked.connect(self.editor.sharpen)
        self.BW_button = QPushButton("B/W")
        self.BW_button.clicked.connect(self.editor.gray)
        self.colour_button = QPushButton("Colour")
        self.colour_button.clicked.connect(self.editor.enhance_colour)
        self.contrast_button = QPushButton("Contrast")
        self.contrast_button.clicked.connect(self.editor.contrast)

        # --- Layouts ---
        # Sidebar with controls
        function_layout = QVBoxLayout()
        function_layout.addWidget(self.select_folder_button)
        function_layout.addWidget(self.file_list)
        function_layout.addWidget(self.function_select_box)
        function_layout.addWidget(self.left_button)
        function_layout.addWidget(self.right_button)
        function_layout.addWidget(self.mirror_button)
        function_layout.addWidget(self.sharpness_button)
        function_layout.addWidget(self.BW_button)
        function_layout.addWidget(self.colour_button)
        function_layout.addWidget(self.contrast_button)

        # Main layout: sidebar + image zone
        main_layout = QHBoxLayout()
        main_layout.addLayout(function_layout, 20)
        main_layout.addWidget(self.image_zone, 80)

        # Set up the main window
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
        
        # Working directory
        self.work_dir = ""
    
    def filter(self, files, extensions):
        res = []
        for file in files:
            for extension in extensions:
                if file.endswith(extension):
                    res.append(file)
        return res
    
    # Choose current work directory
    def get_work_directory(self):
        self.work_dir = QFileDialog.getExistingDirectory()
        extensions = [".jpg", ".jpeg", ".png", ".svg"]
        filenames = self.filter(os.listdir(self.work_dir), extensions)
        self.file_list.clear()
        for filename in filenames:
            self.file_list.addItem(filename)
            
    def display_image(self):
        if self.file_list.currentRow() >= 0:
            filename = self.file_list.currentItem().text()
            self.editor.load_image(filename)
            self.editor.show_image(os.path.join(self.work_dir, self.editor.filename))


class Editor():
    def __init__(self, main_app):
        self.main_app = main_app
        self.image = None
        self.original_image = None
        self.filename = None
        self.save_folder = "edits/"
        
    def load_image(self, filename):
        self.filename = filename
        fullname = os.path.join(self.main_app.work_dir, self.filename)
        self.image = Image.open(fullname)
        self.original_image = self.image.copy()
    
    def save_image(self):
        path = os.path.join(self.main_app.work_dir, self.save_folder)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)
        
    def show_image(self, path):
        self.main_app.image_zone.hide()
        image = QPixmap(path)
        width = self.main_app.image_zone.width()
        height = self.main_app.image_zone.height()
        image = image.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio)
        self.main_app.image_zone.setPixmap(image)
        self.main_app.image_zone.show()
    
    def gray(self):
        self.image = self.image.convert("L")
        self.save_image()
        image_path = os.path.join(self.main_app.work_dir, self.save_folder, self.filename)
        self.show_image(image_path)
        
    def left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.save_image()
        image_path = os.path.join(self.main_app.work_dir, self.save_folder, self.filename)
        self.show_image(image_path)
    
    def right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.save_image()
        image_path = os.path.join(self.main_app.work_dir, self.save_folder, self.filename)
        self.show_image(image_path)
        
    def mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
        image_path = os.path.join(self.main_app.work_dir, self.save_folder, self.filename)
        self.show_image(image_path)
    
    def sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.save_image()
        image_path = os.path.join(self.main_app.work_dir, self.save_folder, self.filename)
        self.show_image(image_path)
        
    def blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.save_image()
        image_path = os.path.join(self.main_app.work_dir, self.save_folder, self.filename)
        self.show_image(image_path)
    
    def enhance_colour(self):
        self.image = ImageEnhance.Color(self.image).enhance(1.2)
        self.save_image()
        image_path = os.path.join(self.main_app.work_dir, self.save_folder, self.filename)
        self.show_image(image_path)
    
    def contrast(self):
        self.image = ImageEnhance.Contrast(self.image).enhance(1.2)
        self.save_image()
        image_path = os.path.join(self.main_app.work_dir, self.save_folder, self.filename)
        self.show_image(image_path)
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())