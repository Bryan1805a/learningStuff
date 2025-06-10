import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMouseTracking(True)
        self.label = QLabel("Click in this window")
        self.label.setMouseTracking(True)
        self.setCentralWidget(self.label)

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mousePressEvent LEFT")
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mousePressEvent MIDDLE")
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mousePressEvent RIGHT")
    
    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseDouble LEFT")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()