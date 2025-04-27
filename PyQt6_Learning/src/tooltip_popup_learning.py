import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tooltip and Popup")
        self.resize(400, 200)

        