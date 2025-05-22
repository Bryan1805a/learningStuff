from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                             QLineEdit, QGridLayout, QPushButton)
from PyQt6.QtCore import Qt
import sys

class CalculatorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 400)

        # Central widget and main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Create UI element
        self._create_display()
        self._create_button()
    
    def _create_display(self):
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 24px;")
        self.display.setMinimumHeight(50)
        self.main_layout.addWidget(self.display)

    def _create_button(self):
        self.buttons_layout = QGridLayout()

        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '(',
            '1', '2', '3', '-', ')',
            '0', '.', '=', '+', '⌫'
        ]

        positions = [(i, j) for i in range(4) for j in range(5)]
        for position, text in zip(positions, buttons):
            button = QPushButton(text)
            button.setStyleSheet("font-size: 18px;")
            button.setMinimumHeight(40)
            self.buttons_layout.addWidget(button, *position)
        
        self.main_layout.addLayout(self.buttons_layout)
    
    def get_display_text(self):
        return self.display.text()
    
    def set_display_text(self, text):
        self.display.setText(text)
        self.display.setFocus()
    
    def clear_display(self):
        self.set_display_text("")