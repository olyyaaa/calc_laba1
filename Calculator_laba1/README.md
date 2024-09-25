This project is a Python-based console calculator that supports basic and advanced arithmetic operations, including addition, subtraction, multiplication, division, exponentiation, square root, and modulus.

# Usage:

Run the program by executing runner.py from the terminal.
Follow the prompts to input two numbers and choose an operator.
The calculator will display the result.
Users can adjust settings like the number of decimal places.
You can view past calculations by answering "yes" when prompted.

# Features:
Basic Arithmetic: Addition (+), Subtraction (-), Multiplication (*), Division (/), Exponentiation (^), Square Root (√), and Modulus (%).
Memory Function: Save and recall previous results.
Customizable Settings: Change the number of decimal places displayed (default is 3).
Error Handling: Manages division by zero and invalid input errors with proper feedback.
Calculation History: Review previous calculations on demand.
Logging: All calculations and errors are logged into log.txt and history.txt.

# File Structure:
runner.py: Main script that runs the calculator.
functions.py: Contains the core logic for performing calculations.
appSettings.py: Stores and manages user-defined settings (e.g., decimal places).
logs/: Directory containing logs and calculation history.
log.txt: Logs all operations and errors.
history.txt: Stores the history of previous calculations.
tests/: Contains unit tests to ensure the accuracy of the calculator's functionality.
