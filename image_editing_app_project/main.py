from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget,
                             QLabel, QPushButton, QListWidget,
                             QComboBox, QVBoxLayout, QHBoxLayout
)
import sys

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Editing App")

        # --- Widgets ---
        # Image display area
        image_zone = QLabel("Image will appear here")

        # Folder selection
        select_folder_button = QPushButton("Select folder")

        # List of objects (images)
        object_list = QListWidget()

        # Function selection dropdown
        function_select_box = QComboBox()
        function_select_box.addItems([
            "Original", "Left", "Right", "Mirror",
            "Sharpness", "B/W", "Colour", "Contrast"
        ])

        # Function buttons
        left_button = QPushButton("Left")
        right_button = QPushButton("Right")
        mirror_button = QPushButton("Mirror")
        sharpness_button = QPushButton("Sharpness")
        BW_button = QPushButton("B/W")
        colour_button = QPushButton("Colour")
        contrast_button = QPushButton("Contrast")

        # --- Layouts ---
        # Sidebar with controls
        function_layout = QVBoxLayout()
        function_layout.addWidget(select_folder_button)
        function_layout.addWidget(object_list)
        function_layout.addWidget(function_select_box)
        function_layout.addWidget(left_button)
        function_layout.addWidget(right_button)
        function_layout.addWidget(mirror_button)
        function_layout.addWidget(sharpness_button)
        function_layout.addWidget(BW_button)
        function_layout.addWidget(colour_button)
        function_layout.addWidget(contrast_button)

        # Main layout: sidebar + image zone
        main_layout = QHBoxLayout()
        main_layout.addLayout(function_layout, 20)
        main_layout.addWidget(image_zone, 80)

        # Set up the main window
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())