from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget,
                             QLabel, QPushButton, QListWidget,
                             QComboBox, QVBoxLayout, QHBoxLayout,
                             QFileDialog
)
import sys
import os

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Editing App")
        self.resize(900, 700)

        # --- Widgets ---
        # Image display area
        self.image_zone = QLabel("Image will appear here")

        # Folder selection
        self.select_folder_button = QPushButton("Select folder")
        self.select_folder_button.clicked.connect(self.get_work_directory)

        # List of objects (images)
        self.file_list = QListWidget()

        # Function selection dropdown
        self.function_select_box = QComboBox()
        self.function_select_box.addItems([
            "Original", "Left", "Right", "Mirror",
            "Sharpness", "B/W", "Colour", "Contrast"
        ])

        # Function buttons
        self.left_button = QPushButton("Left")
        self.right_button = QPushButton("Right")
        self.mirror_button = QPushButton("Mirror")
        self.sharpness_button = QPushButton("Sharpness")
        self.BW_button = QPushButton("B/W")
        self.colour_button = QPushButton("Colour")
        self.contrast_button = QPushButton("Contrast")

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
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())