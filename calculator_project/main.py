from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget,
                             QLineEdit, QPushButton, QLabel,
                             QVBoxLayout, QHBoxLayout, QGridLayout)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Settings
        self.setWindowTitle("Calculator")
        self.resize(300, 200)

        # Objects
        text_box = QLineEdit()
        text_box.setReadOnly(True)

        buttons = [
            "7", "8", "9"
        ]
        # Layouts

        # Function


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())