import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tooltip and Popup")
        self.resize(400, 200)

        self.label = QLabel("Hover your mouse here", self)
        self.label.setToolTip("This is the tooltip")

        self.button = QPushButton("Show popup", self)
        self.button.setToolTip("Click to showi popup")
        self.button.clicked.connect(self.show_popup)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Notification")
        msg.setText("You've clicked the button")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())