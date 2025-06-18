# Modules
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QPushButton,
                             QMainWindow)
from random import choice
import sys

class MainWindow(QMainWindow):
    # Settings
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Word Maker")
        self.resize(300, 200)

        # Objects
        app_label = QLabel("Random Word Maker")

        self.text_1 = QLabel("?")
        self.text_2 = QLabel("?")
        self.text_3 = QLabel("?")

        button_1 = QPushButton("Click")
        button_2 = QPushButton("Click")
        button_3 = QPushButton("Click")

        self.words = ["A", "B", "C", "D", "E", "F"]

        # Layout
        main_layout = QVBoxLayout()
        sub_layout_0 = QHBoxLayout()
        sub_layout_1 = QHBoxLayout()
        sub_layout_2 = QHBoxLayout()

        sub_layout_0.addWidget(app_label, alignment=Qt.AlignmentFlag.AlignCenter)

        sub_layout_1.addWidget(self.text_1, alignment=Qt.AlignmentFlag.AlignCenter)
        sub_layout_1.addWidget(self.text_2, alignment=Qt.AlignmentFlag.AlignCenter)
        sub_layout_1.addWidget(self.text_3, alignment=Qt.AlignmentFlag.AlignCenter)

        sub_layout_2.addWidget(button_1)
        sub_layout_2.addWidget(button_2)
        sub_layout_2.addWidget(button_3)

        main_layout.addLayout(sub_layout_0)
        main_layout.addLayout(sub_layout_1)
        main_layout.addLayout(sub_layout_2)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Event Connections
        button_1.clicked.connect(self.random_word_1)
        button_2.clicked.connect(self.random_word_2)
        button_3.clicked.connect(self.random_word_3)

    # Functions
    def random_word_1(self):
        chose_word = choice(self.words)
        self.text_1.setText(chose_word)

    def random_word_2(self):
        chose_word = choice(self.words)
        self.text_2.setText(chose_word)
    
    def random_word_3(self):
        chose_word = choice(self.words)
        self.text_3.setText(chose_word)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())