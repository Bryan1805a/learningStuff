import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QMenu
from PyQt6.QtCore import Qt

class WordListApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Word List Example")
        self.resize(400, 300)

        self.label = QLabel("Choose a word from the list:", self)

        self.word_list = QListWidget(self)
        self.words_dict = {"Eloquent": "Eloquent = Giỏi ăn nói, hùng biện",
                          "Benevolent": "Benevolent = Nhân hậu, rộng lượng",
                          "Candid": "Candid = Thẳng thắn, không thiên vị",
                          "Deliberate": "Deliberate = Thận trọng, cẩn thận",
                          "Abberation": "Abberation = Hoảng loạn"}
        self.word_list.addItems(self.words_dict)
        # Right click
        self.word_list.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.word_list.customContextMenuRequested.connect(self.open_context_menu)

        # Clear button
        self.clear_button = QPushButton("Clear all", self)
        self.clear_button.clicked.connect(self.clear_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.word_list)
        layout.addWidget(self.clear_button)
        self.setLayout(layout)

    def clear_button_clicked(self):
        self.label.clear()
        self.word_list.clear()

    def open_context_menu(self, position):
        item = self.word_list.itemAt(position)
        if item:
            menu = QMenu(self)
            view_action = menu.addAction("View Definition")
            delete_action = menu.addAction("Delete word")

            action = menu.exec(self.word_list.mapToGlobal(position))

            if action == view_action:
                self.label.setText(f"Definition: {self.words_dict[item.text()]}")
            elif action == delete_action:
                self.words_dict.pop(item.text(), None)
                self.word_list.takeItem(self.word_list.row(item))

app = QApplication(sys.argv)
window = WordListApp()
window.show()
sys.exit(app.exec())