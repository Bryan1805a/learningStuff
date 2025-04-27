import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget

class WordListApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Word List Example")
        self.resize(400, 300)

        self.label = QLabel("Choose a word from the list:", self)

        self.word_list = QListWidget(self)
        self.word_list.addItems(["aberration", "benevolent", "candid", "deliberate", "eliquent"])
        self.word_list.itemClicked.connect(self.on_item_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.word_list)
        self.setLayout(layout)

    def on_item_clicked(self, item):
        word = item.text()
        self.label.setText(f"You choose: {word}")

app = QApplication(sys.argv)
window = WordListApp()
window.show()
sys.exit(app.exec())