from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QStackedWidget

class HomeScreen(QWidget):
    def __init__(self, switch_function):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("🎮 Welcome to the Prank App")
        button1 = QPushButton("Start Game")
        button1.clicked.connect(switch_function)
        layout.addWidget(label)
        layout.addWidget(button1)
        self.setLayout(layout)


class GameScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("This is the game screen.")
        layout.addWidget(label)
        self.setLayout(layout)


class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.home = HomeScreen(self.show_game_screen)
        self.game = GameScreen()

        self.addWidget(self.home)  # Index 0
        self.addWidget(self.game)  # Index 1

        self.setCurrentIndex(0)  # Show home screen first

    def show_game_screen(self):
        self.setCurrentIndex(1)  # Switch to game screen


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("Multi-Screen App")
    window.resize(400, 200)
    window.show()
    app.exec()
