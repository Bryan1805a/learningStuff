import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set window title
        self.setWindowTitle("QT signals and Slots")

        # Create a button and connect it to a method
        button = QPushButton("Click me")
        button.clicked.connect(self.button_clicked)

        # Place the widgets using a vertical box layout
        layout = QVBoxLayout()
        layout.addWidget(button)

        self.setLayout(layout)

        self.show()
    
    def button_clicked(self):
        print("clicked")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create main window
    window = MainWindow()
    sys.exit(app.exec())