import sys
from layout_colorwidget import Color
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QHBoxLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        layout_1 = QHBoxLayout()
        layout_2 = QVBoxLayout()
        layout_3 = QVBoxLayout()

        layout_2.addWidget(Color("red"))
        layout_2.addWidget(Color("yellow"))
        layout_2.addWidget(Color("purple"))

        layout_1.addLayout(layout_2)

        layout_1.addWidget(Color("green"))

        layout_3.addWidget(Color("red"))
        layout_3.addWidget(Color("purple"))

        layout_1.addLayout(layout_3)

        widget = QWidget()
        widget.setLayout(layout_1)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()