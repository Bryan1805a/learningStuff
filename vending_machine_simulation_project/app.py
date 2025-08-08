import sys
from pathlib import Path
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel,
                               QLineEdit, QListWidget, QHBoxLayout, QListWidgetItem, QTextEdit)


class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.create_widgets()
        self.setup_layouts()
        
    def setup_window(self):
        """Configure main window properties"""
        self.setWindowTitle("Vending Machine")
        self.setGeometry(100, 100, 600, 400)

    def create_widgets(self):
        """Create all UI widgets"""
        self._create_title_label()
        self._create_money_entry()
        self._create_product_list()
        self._create_status_panel()
        self._create_buttons()
        
    def _create_title_label(self):
        """Create the main title label"""
        self.label = QLabel("VENDING MACHINE")
        self.label.setObjectName("machine_label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def _create_money_entry(self):
        """Create money input widgets"""
        self.money_amount_entry_label = QLabel("Enter amount:")
        self.money_amount_entry = QLineEdit()
        self.money_amount_entry.setClearButtonEnabled(True)
        
        # Set up validator for integers only
        money_validator = QIntValidator(0, 99999999)
        self.money_amount_entry.setValidator(money_validator)

    def _create_product_list(self):
        """Create and populate the product list"""
        self.product_list = QListWidget()
        
        # Product data
        products = [
            ("Coca Cola", 25), 
            ("Orange Juice", 15), 
            ("Pepsi", 25),
            ("Coffee", 12), 
            ("Fresh Water", 8), 
            ("Tea", 10)
        ]
        
        # Add products to list
        for name, price in products:
            item = QListWidgetItem(f"{name} - ${price}")
            item.setData(Qt.ItemDataRole.UserRole, {"name": name, "price": price})
            self.product_list.addItem(item)

    def _create_status_panel(self):
        """Create the status display panel"""
        self.status_panel = QTextEdit()
        self.status_panel.setText(
            "Your amount: \n"
            "Your choice: \n"
            "\n"
            "STATUS: \n"
            "Your change: "
        )

    def _create_buttons(self):
        """Create action buttons and labels"""
        self.confirm_button = QPushButton("CONFIRM")
        self.cancel_button = QPushButton("CANCEL")
        self.cancel_note_label = QLabel("You will receive all money back if you press CANCEL")

    def setup_layouts(self):
        """Setup and arrange all layouts"""
        # Create main container
        container = QWidget()
        main_layout = QVBoxLayout()
        
        # Add title
        main_layout.addWidget(self.label)
        
        # Create and add the main content area
        content_layout = self._create_content_layout()
        main_layout.addLayout(content_layout)
        
        # Set up container
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def _create_content_layout(self):
        """Create the main content layout with left and right sections"""
        content_layout = QHBoxLayout()
        
        # Left side - Input and product selection
        left_layout = self._create_left_layout()
        content_layout.addLayout(left_layout)
        
        # Right side - Status and buttons
        right_layout = self._create_right_layout()
        content_layout.addLayout(right_layout)
        
        return content_layout

    def _create_left_layout(self):
        """Create left side layout (money entry + product list)"""
        left_layout = QVBoxLayout()
        
        # Money entry section
        money_layout = QHBoxLayout()
        money_layout.addWidget(self.money_amount_entry_label)
        money_layout.addWidget(self.money_amount_entry)
        
        left_layout.addLayout(money_layout)
        left_layout.addWidget(self.product_list)
        
        return left_layout

    def _create_right_layout(self):
        """Create right side layout (status panel + buttons)"""
        right_layout = QVBoxLayout()
        
        # Status panel
        right_layout.addWidget(self.status_panel)
        
        # Buttons section
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.confirm_button)
        buttons_layout.addWidget(self.cancel_button)
        
        right_layout.addLayout(buttons_layout)
        right_layout.addWidget(self.cancel_note_label)
        
        return right_layout


def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    window = DemoWindow()

    # Load stylesheet if exists
    qss_path = Path("style.qss")
    if qss_path.exists():
        with open(qss_path, 'r') as f:
            app.setStyleSheet(f.read())

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()