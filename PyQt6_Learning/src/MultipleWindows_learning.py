import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.resize(400, 300)

        # Counter variable
        self.settings_open_count = 0

        # Counter label
        self.settings_window_open_counter_label = QLabel(f"Settings opened: 0 times", self)

        # Open word info button
        self.open_word_info_button = QPushButton("Open Word Info", self)
        self.open_word_info_button.clicked.connect(self.open_word_info_window)

        # Open Setting button
        self.open_settings_button = QPushButton("Open Settings", self)
        self.open_settings_button.clicked.connect(self.open_settings_window)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.settings_window_open_counter_label)
        layout.addWidget(self.open_word_info_button)
        layout.addWidget(self.open_settings_button)
        self.setLayout(layout)

    # Open Word Information Window
    def open_word_info_window(self):
        self.word_info_window = WordInformationWindow()
        self.word_info_window.show()

    # Open Settings Window
    def open_settings_window(self):
        self.settings_open_count += 1
        count_text = "time" if self.settings_open_count == 1 else "times"
        self.settings_window_open_counter_label.setText(f"Settings opened: {self.settings_open_count} {count_text}")
        
        self.settings_window = SettingsWindow()
        self.settings_window.show()


class WordInformationWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Word Information")
        self.resize(200, 100)

        # Label
        self.welcome_label = QLabel("Welcome to Word Information!", self)

        # Close window button
        self.close_window_button = QPushButton("Close", self)
        self.close_window_button.clicked.connect(self.close_window)

        # Layout 
        layout = QVBoxLayout()
        layout.addWidget(self.welcome_label)
        layout.addWidget(self.close_window_button)
        self.setLayout(layout)
    
    def close_window(self):
        self.close()


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Settings")
        self.resize(200, 100)

        # Label
        self.welcome_label = QLabel("This is the Settings Window!", self)

        # Close window button
        self.close_window_button = QPushButton("Close", self)
        self.close_window_button.clicked.connect(self.close_window)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.welcome_label)
        layout.addWidget(self.close_window_button)
        self.setLayout(layout)

    def close_window(self):
        self.close()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())