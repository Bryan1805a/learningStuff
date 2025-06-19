from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget,
                             QLineEdit, QPushButton, QLabel,
                             QVBoxLayout, QHBoxLayout, QGridLayout)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Settings
        self.setWindowTitle("Calculator")
        self.resize(100, 300)

        # Objects
        self.text_box = QLineEdit()
        self.text_box.setReadOnly(True)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "<", "+"
        ]
        clear_button = QPushButton("CLEAR")
        clear_button.clicked.connect(self.button_clicked)
        result_button = QPushButton("=")
        result_button.clicked.connect(self.button_clicked)

        # Layouts
        main_layout = QVBoxLayout()
        button_layout = QGridLayout()
        button_layout_2 = QHBoxLayout()

        main_layout.addWidget(self.text_box)

        # Set button for button_layout
        row = 0
        col = 0
        for i in buttons:
            button = QPushButton(i)
            button_layout.addWidget(button, row, col)
            button.clicked.connect(self.button_clicked)
            col += 1

            if col > 3:
                row += 1
                col = 0
        
        button_layout_2.addWidget(clear_button)
        button_layout_2.addWidget(result_button)

        
        main_layout.addLayout(button_layout)
        main_layout.addLayout(button_layout_2)

        container = QWidget()
        container.setLayout(main_layout)

        self.setCentralWidget(container)

        # Function
    def button_clicked(self):
        button = app.sender()
        text = button.text()

        if text == "=":
            symbol = self.text_box.text()
            try:
                res = eval(symbol)
                self.text_box.setText(str(res))
            except Exception as e:
                self.text_box.setText("Error")

        elif text == "CLEAR":
            self.text_box.clear()

        elif text == "<":
            current_text = self.text_box.text()
            self.text_box.setText(current_text[:-1])

        else:
            current_text = self.text_box.text()
            self.text_box.setText(current_text + text)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())