import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel
app = QApplication(sys.argv)

a = QMainWindow()
print(a.centralWidget())

a.show()
app.exec()