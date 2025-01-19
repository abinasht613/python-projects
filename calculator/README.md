# Test Cases for the Calculator
We will test the logic for:

1. Basic arithmetic operations (+, -, *, /).
2. Edge cases (e.g., division by zero).
3. Display updates when buttons are clicked.
4. Error handling.

# How It Works
1. Setup with setUp():
    * Initializes the Calculator object before each test.
2. Helper Method click_button():
    * Simulates button clicks by searching for buttons by their text.
3. Individual Test Cases:
    * Each test case verifies a specific functionality or edge case.


# Run:
* python -m unittest test_calculator.py

# Advantages of Automated Tests
1. Ensures the calculator's core logic works as expected.
2. Prevents regressions when making changes to the code.
3. Makes the application more robust and production-ready.
