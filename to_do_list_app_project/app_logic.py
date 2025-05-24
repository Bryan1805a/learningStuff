from PyQt6.QtWidgets import (QApplication, QListWidgetItem, QMessageBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QColor

class AppLogic:
    def __init__(self, ui):
        self.ui = ui
        self.connect_signals()

    def connect_signals(self):
        self.ui.task_input.returnPressed.connect(self.add_task)
        self.ui.add_button.clicked.connect(self.add_task)
        self.ui.delete_button.clicked.connect(self.delete_task)
        self.ui.clear_button.clicked.connect(self.clear_task)
        self.ui.complete_button.clicked.connect(self.mark_complete)

    def add_task(self):
        task_text = self.ui.task_input.text().strip()
        if task_text:
            item = QListWidgetItem(task_text)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.ui.task_list.addItem(item)
            self.ui.task_input.clear()
            self.update_status(f"Task added: {task_text}")
        else:
            self.update_status("Please enter a task")

    def delete_task(self):
        seleted_items = self.ui.task_list.selectedItems()
        if not seleted_items:
            self.update_status("No task selected to delete")
            return
        
        for item in seleted_items:
            self.ui.task_list.takeItem(self.ui.task_list.row(item))
            self.update_status("Task deleted")

    def clear_task(self):
        if self.ui.task_list.count() == 0:
            self.update_status("No task to clear")
            return
        
        reply = QMessageBox.question(
            self.ui, "Clear All", "Are you sure you want to clear all task?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.ui.task_list.clear()
            self.update_status("All tasks cleared")
        
    def mark_complete(self):
        selected_items = self.ui.task_list.selectedItems()
        if not selected_items:
            self.update_status("No task selected to mark complete")
            return
        
        for item in selected_items:
            item.setCheckState(Qt.CheckState.Checked)
            item.setForeground(QBrush(QColor(100, 100, 100)))
            item.setFlags(~Qt.ItemFlag.ItemIsSelectable & item.flags())
            self.update_status("Task marked as complete")

    
    def update_status(self, message):
        self.ui.status_label.setText(message)