import sys
import chat_messages
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QHBoxLayout, QGridLayout, QLabel,
                             QLineEdit, QPushButton, QStackedWidget)

class HomeScreen(QWidget):
    def __init__(self, switch_function):
        super().__init__()
        self.switch = switch_function

        # Label layout
        label_layout = QVBoxLayout()
        self.current_message_index = 0
        self.chat_label = QLabel(chat_messages.home_screen_messages[self.current_message_index])

        label_layout.addWidget(self.chat_label)

        # Button Label
        button_layout = QHBoxLayout()
        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next_button_clicked)
        self.previous_button = QPushButton("Previous")
        self.previous_button.clicked.connect(self.previous_button_clicked)

        button_layout.addWidget(self.previous_button)
        button_layout.addWidget(self.next_button)
        
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(label_layout)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    # Switch Messages and HomeScreen method
    def next_button_clicked(self):
        if self.current_message_index >= chat_messages.len_HSM:
            self.switch()
            return
        self.current_message_index += 1
        self.chat_label.setText(chat_messages.home_screen_messages[self.current_message_index])

    def previous_button_clicked(self):
        if self.current_message_index == 0:
            return
        self.current_message_index -= 1
        self.chat_label.setText(chat_messages.home_screen_messages[self.current_message_index])

class GameScreen(QWidget):
    def __init__(self, switch_function):
        super().__init__()
        self.switch = switch_function

        # Label layout
        label_layout = QVBoxLayout()
        self.current_message_index = 0
        self.chat_label = QLabel(chat_messages.game_screen_messages[self.current_message_index])

        label_layout.addWidget(self.chat_label)

        # Button layout
        button_layout = QHBoxLayout()
        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next_button_clicked)
        self.previous_button = QPushButton("Previous")
        self.previous_button.clicked.connect(self.previous_button_clicked)

        button_layout.addWidget(self.previous_button)
        button_layout.addWidget(self.next_button)

        # Choice button layout
        choice_button_layout = QGridLayout()
        self.button_1 = QPushButton("Button 1")
        self.button_2 = QPushButton("Button 2")
        self.button_3 = QPushButton("Button 3")
        self.button_4 = QPushButton("Button 4")
        self.button_5 = QPushButton("Button 5")
        self.button_6 = QPushButton("Button 6")

        choice_button_layout.addWidget(self.button_1, 0, 0)
        choice_button_layout.addWidget(self.button_2, 0, 1)
        choice_button_layout.addWidget(self.button_3, 0, 2)
        choice_button_layout.addWidget(self.button_4, 1, 0)
        choice_button_layout.addWidget(self.button_5, 1, 1)
        choice_button_layout.addWidget(self.button_6, 1, 2)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(label_layout)
        main_layout.addLayout(button_layout)
        main_layout.addLayout(choice_button_layout)
        self.setLayout(main_layout)

    def next_button_clicked(self):
        self.current_message_index += 1
        self.chat_label.setText(chat_messages.game_screen_messages[self.current_message_index])

    def previous_button_clicked(self):
        if self.current_message_index <= 0:
            self.switch()
            return
        self.current_message_index -= 1
        self.chat_label.setText(chat_messages.game_screen_messages[self.current_message_index])

class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.home = HomeScreen(self.switch_game_screen)
        self.game = GameScreen(self.switch_home_screen)

        self.addWidget(self.home)
        self.addWidget(self.game)

        self.setCurrentIndex(0)

    def switch_game_screen(self):
        self.setCurrentIndex(1)

    def switch_home_screen(self):
        self.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("A small cheap prank")
    window.resize(600, 300)
    window.show()
    sys.exit(app.exec())