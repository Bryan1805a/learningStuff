import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My app")

        button = QPushButton("Clich me!")
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

    def button_clicked(self):
        print("Button was clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())