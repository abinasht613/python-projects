import unittest 
from PyQt6.QtWidgets import QApplication, QPushButton  
from calculator import Calculator  # Assuming the main calculator code is in a file named `calculator.py`

# Create an instance of QApplication
app = QApplication([]) # Create a QApplication instance

class TestCalculator(unittest.TestCase): # Create a test class that inherits from unittest.TestCase
    def setUp(self):            # Create a setUp method to set up the Calculator app for testing
        """Set up the Calculator app for testing."""
        self.calc = Calculator()

    def click_button(self, button_text):        # Create a helper function to simulate button clicks
        """Helper function to simulate button clicks."""    # The helper function takes a button text as input
        for button in self.calc.centralWidget().findChildren(QPushButton): # Iterate over all QPushButton widgets in the Calculator app
            if button.text() == button_text:
                button.click()
                break

    def test_addition(self):
        """Test addition functionality."""
        self.click_button('1')
        self.click_button('+')
        self.click_button('2')
        self.click_button('=')
        self.assertEqual(self.calc.display.text(), '3') # Check if the display text is '3'

    def test_subtraction(self):
        """Test subtraction functionality."""
        self.click_button('5')
        self.click_button('-')
        self.click_button('3')
        self.click_button('=')
        self.assertEqual(self.calc.display.text(), '2')

    def test_multiplication(self):
        """Test multiplication functionality."""
        self.click_button('4')
        self.click_button('*')
        self.click_button('5')
        self.click_button('=')
        self.assertEqual(self.calc.display.text(), '20')

    def test_division(self):
        """Test division functionality."""
        self.click_button('8')
        self.click_button('/')
        self.click_button('4')
        self.click_button('=')
        self.assertEqual(self.calc.display.text(), '2.0')

    def test_division_by_zero(self):
        """Test division by zero handling."""
        self.click_button('5')
        self.click_button('/')
        self.click_button('0')
        self.click_button('=')
        self.assertEqual(self.calc.display.text(), 'Error')

    def test_clear(self):
        """Test the clear button functionality."""
        self.click_button('9')
        self.click_button('C')
        self.assertEqual(self.calc.display.text(), '')

    def test_decimal_point(self):
        """Test decimal point usage."""
        self.click_button('7')
        self.click_button('.')
        self.click_button('5')
        self.click_button('+')
        self.click_button('2')
        self.click_button('=')
        self.assertEqual(self.calc.display.text(), '9.5')

    def test_invalid_expression(self):
        """Test handling of invalid expressions."""
        self.click_button('+')
        self.click_button('=')
        self.assertEqual(self.calc.display.text(), 'Error')

if __name__ == "__main__":
    unittest.main()
