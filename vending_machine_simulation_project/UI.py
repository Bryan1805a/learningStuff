from PySide6.QtGui import QIntValidator
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel,
                               QLineEdit, QListWidget, QHBoxLayout, QListWidgetItem, QTextEdit)

# Import your backend
from backend import VendingMachine


class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Initialize backend
        self.vending_machine = VendingMachine()
        
        self.setup_window()
        self.create_widgets()
        self.setup_layouts()
        self.connect_signals()
        self.update_display()
        
    def setup_window(self):
        self.setWindowTitle("Vending Machine")
        self.setGeometry(100, 100, 600, 400)

    def create_widgets(self):
        self._create_title_label()
        self._create_money_entry()
        self._create_product_list()
        self._create_status_panel()
        self._create_buttons()
        
    def _create_title_label(self):
        self.label = QLabel("VENDING MACHINE")
        self.label.setObjectName("machine_label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def _create_money_entry(self):
        self.money_amount_entry_label = QLabel("Enter amount:")
        self.money_amount_entry = QLineEdit()
        self.money_amount_entry.setClearButtonEnabled(True)
        
        # Set up validator for integers only
        money_validator = QIntValidator(0, 99999999)
        self.money_amount_entry.setValidator(money_validator)

    def _create_product_list(self):
        self.product_list = QListWidget()
        self.populate_product_list()

    def populate_product_list(self):
        self.product_list.clear()
        products = self.vending_machine.get_products()
        
        for product in products:
            display_text = f"{product['name']} - ${product['price']} (Stock: {product['stock']})"
            item = QListWidgetItem(display_text)
            item.setData(Qt.ItemDataRole.UserRole, product)
            self.product_list.addItem(item)

    def _create_status_panel(self):
        self.status_panel = QTextEdit()
        self.status_panel.setReadOnly(True)  # Make it read-only

    def _create_buttons(self):
        self.add_money_button = QPushButton("ADD MONEY")
        self.confirm_button = QPushButton("CONFIRM PURCHASE")
        self.cancel_button = QPushButton("CANCEL")
        self.cancel_note_label = QLabel("You will receive all money back if you press CANCEL")

    def connect_signals(self):
        self.add_money_button.clicked.connect(self.add_money)
        self.confirm_button.clicked.connect(self.confirm_purchase)
        self.cancel_button.clicked.connect(self.cancel_transaction)
        self.product_list.itemClicked.connect(self.select_product)

    def add_money(self):
        money_text = self.money_amount_entry.text()
        if money_text:
            amount = int(money_text)
            if self.vending_machine.insert_money(amount):
                self.money_amount_entry.clear()
                self.update_display()

    def select_product(self, item):
        product_data = item.data(Qt.ItemDataRole.UserRole)
        self.vending_machine.select_product(product_data["name"])
        self.update_display()

    def confirm_purchase(self):
        success, message, change = self.vending_machine.purchase()
        
        if success:
            self.populate_product_list()  # Refresh stock display
        
        self.update_display(message, change if success else None)

    def cancel_transaction(self):
        refund = self.vending_machine.cancel_transaction()
        message = f"Transaction cancelled. Refunded: ${refund}" if refund > 0 else "Transaction cancelled."
        self.update_display(message)

    def update_display(self, message="", change=None):
        status = self.vending_machine.get_status()
        
        display_text = f"Your amount: ${status['inserted_money']}\n"
        display_text += f"Your choice: {status['selected_product'] or 'None'}\n"
        
        if status['selected_product']:
            display_text += f"Price: ${status['selected_price']}\n"
        
        display_text += "\nSTATUS:\n"
        
        if message:
            display_text += f"{message}\n"
        else:
            can_buy, status_msg = self.vending_machine.can_purchase()
            display_text += f"{status_msg}\n"
        
        if change is not None:
            display_text += f"Your change: ${change}"
        
        self.status_panel.setText(display_text)

    def setup_layouts(self):
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
        content_layout = QHBoxLayout()
        
        # Left side - Input and product selection
        left_layout = self._create_left_layout()
        content_layout.addLayout(left_layout)
        
        # Right side - Status and buttons
        right_layout = self._create_right_layout()
        content_layout.addLayout(right_layout)
        
        return content_layout

    def _create_left_layout(self):
        left_layout = QVBoxLayout()
        
        # Money entry section
        money_layout = QHBoxLayout()
        money_layout.addWidget(self.money_amount_entry_label)
        money_layout.addWidget(self.money_amount_entry)
        money_layout.addWidget(self.add_money_button)
        
        left_layout.addLayout(money_layout)
        left_layout.addWidget(self.product_list)
        
        return left_layout

    def _create_right_layout(self):
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


