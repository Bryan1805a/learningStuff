from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QLabel, QLineEdit, QListWidget,
                             QPushButton, QVBoxLayout, QHBoxLayout)

class AppUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App")
        self.setFixedSize(400, 500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Title
        self.title_label = QLabel("To-Do List")
        self.title_label.setObjectName("titleLabel")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.main_layout.addWidget(self.title_label)

        """ Input area """
        self.input_layout = QHBoxLayout()

        # Input box
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a new task...")
        self.task_input.setObjectName("taskInput")
        self.input_layout.addWidget(self.task_input)
        
        # Add button
        self.add_button = QPushButton("Add")
        self.add_button.setObjectName("addButton")
        self.input_layout.addWidget(self.add_button)

        self.main_layout.addLayout(self.input_layout)

        # Task list
        self.task_list = QListWidget()
        self.task_list.setObjectName("taskList")
        self.main_layout.addWidget(self.task_list)

        """ Button area """
        self.button_layout = QHBoxLayout()

        # Delete button
        self.delete_button = QPushButton("Delete")
        self.delete_button.setObjectName("deleteButton")
        self.button_layout.addWidget(self.delete_button)

        # Clear button
        self.clear_button = QPushButton("Clear")
        self.clear_button.setObjectName("clearButton")
        self.button_layout.addWidget(self.clear_button)

        # Complete button
        self.complete_button = QPushButton("Complete")
        self.complete_button.setObjectName("completeButton")
        self.button_layout.addWidget(self.complete_button)

        self.main_layout.addLayout(self.button_layout)

        # Status label
        self.status_label = QLabel("")
        self.status_label.setObjectName("statusLabel")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.main_layout.addWidget(self.status_label)