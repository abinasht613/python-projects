import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QGridLayout # type: ignore

class Calculator(QMainWindow):
    def __init__(self):     # Constructor
        super().__init__()  # Call the parent class constructor
        self.setWindowTitle("Simple Calculator")    # Set the window title
        self.setGeometry(100, 100, 300, 400)        # Set the window geometry

        # Main layout
        self.central_widget = QWidget()             # Create a central widget
        self.setCentralWidget(self.central_widget)  # Set the central widget
        self.layout = QVBoxLayout(self.central_widget)# Create a vertical layout

        # Display field
        self.display = QLineEdit()                      # Create a QLineEdit widget
        self.display.setReadOnly(True)          # Make the display field read-only
        self.display.setStyleSheet("font-size: 20px; padding: 10px;")   # Styling
        self.layout.addWidget(self.display)     # Add the display field to the layout

        # Button grid
        self.create_buttons()       # Create the buttons

    def create_buttons(self):       # Create the buttons
        button_layout = QGridLayout()   # Create a QGridLayout for the buttons

        buttons = [                     # List of buttons with their text and position
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('C', 3, 2), ('+', 3, 3),
            ('=', 4, 0, 1, 4)  # Span the "=" button across 4 columns
        ]

        for btn_text, row, col, *span in buttons:           # Iterate over the buttons
            button = QPushButton(btn_text)                  # Create a QPushButton with the text
            button.setStyleSheet("font-size: 18px; padding: 15px;") # Styling
            button.clicked.connect(self.on_button_click)            # Connect the button click event
            button_layout.addWidget(button, row, col, *(span if span else [1, 1])) # Add the button to the layout

        self.layout.addLayout(button_layout)

    def on_button_click(self):  # Handle button clicks
        button = self.sender()
        text = button.text()

        if text == "C":
            self.display.clear()
        elif text == "=":
            try:
                result = eval(self.display.text())  # Evaluate the expression
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("Error")
        else:
            print(self.display.text() +"--"+ text)
            self.display.setText(self.display.text() + text)    # Append the text to the display field

def main():
    app = QApplication(sys.argv) # Create the application
    calculator = Calculator()    # Create the main window
    calculator.show()            # Display the main window
    sys.exit(app.exec())         # Execute the application

if __name__ == "__main__":       # Run the main function
    main()                       # Run the main function
