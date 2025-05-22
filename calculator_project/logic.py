from PyQt6.QtWidgets import QApplication, QPushButton
from UI import CalculatorUI
import sys
from PyQt6.QtCore import QFile, QTextStream

class Calculator(CalculatorUI):
    def __init__(self):
        super().__init__()
        self._load_stylesheet()
        self._connect_buttons()
        self.current_input = ""

    def _load_stylesheet(self):
        file = QFile("style.qss")
        if file.open(QFile.OpenModeFlag.ReadOnly):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
            file.close()
    
    def _connect_buttons(self):
        """Connect buttons to their functions"""
        for button in self.findChildren(QPushButton):
            text = button.text()
            
            if text not in {'=', 'C', '⌫'}:
                button.clicked.connect(lambda _, t=text: self._append_to_display(t))
            elif text == '⌫':
                button.clicked.connect(self._backspace)
            elif text == 'C':
                button.clicked.connect(self._clear)
            elif text == '=':
                button.clicked.connect(self._calculate)
    
    def _append_to_display(self, text):
        """Append text to the display"""
        self.current_input += text
        self.set_display_text(self.current_input)
    
    def _backspace(self):
        """Remove last character from display"""
        self.current_input = self.current_input[:-1]
        self.set_display_text(self.current_input)
    
    def _clear(self):
        """Clear the display"""
        self.current_input = ""
        self.clear_display()
    
    def _calculate(self):
        """Evaluate the expression in the display"""
        try:
            result = str(eval(self.current_input))
            self.set_display_text(result)
            self.current_input = result
        except Exception:
            self.set_display_text("Error")
            self.current_input = ""

def main():
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())