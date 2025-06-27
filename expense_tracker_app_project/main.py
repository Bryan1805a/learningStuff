from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit, QComboBox,
    QDateEdit, QTableWidget, QVBoxLayout, 
    QHBoxLayout, QMainWindow
)
import sys

class ExpenseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expense Tracker ver 1.0")
        self.resize(550, 500)
        
        # Objects
        self.date_box = QDateEdit()
        self.dropdown = QComboBox()
        self.amount = QLineEdit()
        self.description = QLineEdit()
        
        self.add_button = QPushButton("Add Expense")
        self.delete_button = QPushButton("Delete Expense")
        
        self.table = QTableWidget()
        self.table.setColumnCount(5) # For ID, date, category, amount, description
        self.table.setHorizontalHeaderLabels(["ID", "Date", "Category", "Amount", "Description"])
        
        # Layout
        self.main_layout = QVBoxLayout()
        self.sub_layout_1 = QHBoxLayout()
        self.sub_layout_2 = QHBoxLayout()
        self.sub_layout_3 = QHBoxLayout()
        
        # Sub_layout_1 design
        self.sub_layout_1.addWidget(QLabel("Date:"))
        self.sub_layout_1.addWidget(self.date_box)
        self.sub_layout_1.addWidget(QLabel("Category:"))
        self.sub_layout_1.addWidget(self.dropdown)
        
        # Sub_layout_2 design
        self.sub_layout_2.addWidget(QLabel("Amount:"))
        self.sub_layout_2.addWidget(self.amount)
        self.sub_layout_2.addWidget(QLabel("Description:"))
        self.sub_layout_2.addWidget(self.description)
        
        # Sub_layout_3 design
        self.sub_layout_3.addWidget(self.add_button)
        self.sub_layout_3.addWidget(self.delete_button)
        
        # Main_layout design
        self.main_layout.addLayout(self.sub_layout_1)
        self.main_layout.addLayout(self.sub_layout_2)
        self.main_layout.addLayout(self.sub_layout_3)
        
        self.main_layout.addWidget(self.table)
        
        container = QWidget()
        container.setLayout(self.main_layout)
        self.setCentralWidget(container)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseApp()
    window.show()
    sys.exit(app.exec())