import sys
import os
from app_UI import AppUI
from app_logic import AppLogic
from PyQt6.QtWidgets import (QApplication)

def load_stylesheet():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    style_path = os.path.join(base_dir, "style.qss")

    with open(style_path, 'r') as f:
        return f.read()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    stylesheet = load_stylesheet()
    app.setStyleSheet(stylesheet)
    
    ui = AppUI()
    logic = AppLogic(ui)
    ui.show()

    sys.exit(app.exec())