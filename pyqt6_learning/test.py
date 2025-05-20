import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout

class MyApp(QWidget):
    def __init__(self, *argv, **kwargs):
        super().__init__(*argv, **kwargs)

        self.setWindowTitle("My App")

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec())