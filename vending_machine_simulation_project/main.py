import sys
from pathlib import Path
from UI import DemoWindow
from PySide6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    window = DemoWindow()

    # Load stylesheet if exists
    qss_path = Path("style.qss")
    if qss_path.exists():
        with open(qss_path, 'r') as f:
            app.setStyleSheet(f.read())

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()