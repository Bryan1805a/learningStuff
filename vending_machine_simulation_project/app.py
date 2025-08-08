import sys
from pathlib import Path
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel,
                               QLineEdit, QListWidget, QHBoxLayout, QListWidgetItem)


class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vending Machine")
        self.setGeometry(100, 100, 600, 400)

        # Vending Machine Label
        self.label = QLabel("VENDING MACHINE")
        self.label.setObjectName("machine_label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Money entry
        self.money_amount_entry = QLineEdit()
        self.money_amount_entry.setClearButtonEnabled(True)
        money_validator = QIntValidator(0, 99999999)
        self.money_amount_entry.setValidator(money_validator)

        # Product list
        products = [("Coca Cola", 25), ("Orange Juice", 15), ("Pepsi", 25),
                    ("Coffee", 12), ("Fresh Water", 8), ("Tea", 10)]
        
        self.product_list = QListWidget()
        for name, price in products:
            item = QListWidgetItem(f"{name} - &{price}")
            item.setData(Qt.ItemDataRole.UserRole, {"name": name, "price": price})
            self.product_list.addItem(item)

        # Layout and container
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.money_amount_entry)
        main_layout.addWidget(self.product_list)
        

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)


app = QApplication(sys.argv)
window = DemoWindow()

qss_path = Path("style.qss")
if qss_path.exists():
    with open(qss_path, 'r') as f:
        app.setStyleSheet(f.read())

window.show()
sys.exit(app.exec())