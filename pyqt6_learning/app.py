import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel,
                               QLineEdit, QListWidget, QHBoxLayout)


class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Demo Window")
        self.setGeometry(100, 100, 600, 400)

        self.label = QLabel("May ban nuoc")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.money_enter = QLineEdit()
        self.money_enter.setPlaceholderText("Nhap so tien...")

        self.product_list = QListWidget()

        self.status_label = QLabel("Status: ")
        self.status = QLabel("")
        self.money_change_label = QLabel("Tien thua:")
        self.change_status = QLabel("")

        main_layout = QVBoxLayout()

        status_layout = QHBoxLayout()
        status_layout.addWidget(self.status_label)
        status_layout.addWidget(self.status)

        money_status_layout = QHBoxLayout()
        money_status_layout.addWidget(self.money_change_label)
        money_status_layout.addWidget(self.change_status)

        main_layout.addWidget(self.label)
        main_layout.addWidget(self.money_enter)
        main_layout.addWidget(self.product_list)
        main_layout.addLayout(status_layout)
        main_layout.addLayout(money_status_layout)

        container = QWidget()
        container.setLayout(main_layout)

        self.setCentralWidget(container)


app = QApplication(sys.argv)
window = DemoWindow()
window.show()
sys.exit(app.exec())