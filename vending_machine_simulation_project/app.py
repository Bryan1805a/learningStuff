import sys
from pathlib import Path
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel,
                               QLineEdit, QListWidget, QHBoxLayout, QListWidgetItem, QTextEdit,
                               )


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
        self.money_amount_entry_label = QLabel("Enter amount:")
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

        # Status panel
        self.status_panel = QTextEdit()
        self.status_panel.setText("Your amount: \n" \
                                  "Your choice: \n" \
                                  "\n" \
                                  "STATUS: \n" \
                                  "Your change: ")
        
        # Confirmation button
        self.confirm_button = QPushButton("CONFIRM")
        self.cancel_button = QPushButton("CANCEL")
        self.cancel_note_label = QLabel("You will receive all money back if you press CANCEL")

        # Layout and container
        main_layout = QVBoxLayout()
        sub_layout = QHBoxLayout()

        information_layout = QVBoxLayout()
        status_layout = QVBoxLayout()

        money_entry_layout = QHBoxLayout()
        money_entry_layout.addWidget(self.money_amount_entry_label)
        money_entry_layout.addWidget(self.money_amount_entry)

        # Confirmation buttons
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.confirm_button)
        buttons_layout.addWidget(self.cancel_button)

        # Information layout
        information_layout.addLayout(money_entry_layout)
        information_layout.addWidget(self.product_list)

        # Status layout
        status_layout.addWidget(self.status_panel)
        status_layout.addLayout(buttons_layout)
        status_layout.addWidget(self.cancel_note_label)

        # Sub layout
        sub_layout.addLayout(information_layout)
        sub_layout.addLayout(status_layout)
        
        # Main layout
        main_layout.addWidget(self.label)
        main_layout.addLayout(sub_layout)
        
        # Container
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