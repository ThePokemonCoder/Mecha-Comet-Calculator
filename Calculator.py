import sys
import math
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt6.QtGui import QFont

class ScientificCalculator(QWidget):
    def __init__(self):
        super().__init__()

        # Window Settings
        self.setWindowTitle("Scientific Calculator")
        self.setGeometry(100, 100, 450, 600)
        self.setStyleSheet("background-color: #2E2E2E;")  # Dark Mode

        # Layout
        self.layout = QVBoxLayout()

        # Display
        self.display = QLineEdit()
        self.display.setFont(QFont("Arial", 24))
        self.display.setStyleSheet("color: white; background-color: #444; border: 2px solid #555; padding: 10px;")
        self.display.setReadOnly(True)
        self.layout.addWidget(self.display)

        # Button Grid
        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        # Button Labels
        buttons = [
            ('1', '2', '3', '/'),
            ('4', '5', '6', '*'),
            ('7', '8', '9', '-'),
            ('0', '.', '=', '+'),
            ('(', ')', 'C', '⌫'),
            ('sin', 'cos', 'tan', 'π'),
            ('asin', 'acos', 'atan', 'e'),
            ('log', 'ln', 'sqrt', '^'),
            ('exp', 'mod', '!', '%')
        ]

        # Memory Storage
        self.memory = 0

        # Button Creation
        for row, values in enumerate(buttons):
            for col, value in enumerate(values):
                button = QPushButton(value)
                button.setFont(QFont("Arial", 16))
                button.setStyleSheet(
                    "background-color: #555; color: white; border: 2px solid #666; padding: 10px;"
                    "border-radius: 5px;"
                )
                button.clicked.connect(lambda checked, v=value: self.on_button_click(v))
                self.grid_layout.addWidget(button, row, col)

        # Final Setup
        self.setLayout(self.layout)

    def on_button_click(self, value):
        """Handles button clicks"""
        if value == "=":
            try:
                expression = self.display.text().replace("^", "**").replace("π", str(math.pi)).replace("e", str(math.e))

                # Handle Factorial (!)
                if "!" in expression:
                    expression = expression.replace("!", "")
                    result = math.factorial(int(eval(expression)))
                else:
                    result = eval(expression, {"math": math, "__builtins__": None})

                self.display.setText(str(result))
            except Exception:
                self.display.setText("Error")

        elif value == "C":
            self.display.clear()
        elif value == "⌫":  # Backspace
            self.display.setText(self.display.text()[:-1])
        elif value in ["sin", "cos", "tan", "asin", "acos", "atan", "log", "ln", "sqrt", "exp"]:
            self.display.setText(self.display.text() + f"math.{value}(")
        elif value == "!":
            self.display.setText(self.display.text() + "!")
        else:
            self.display.setText(self.display.text() + value)

# Run Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = ScientificCalculator()
    calculator.show()
    sys.exit(app.exec())
