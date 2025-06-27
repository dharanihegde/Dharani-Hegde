"""
Problem-1: Calculator Class
A simple calculator that performs basic arithmetic operations.
"""

class Calculator:
    """
    A calculator class that performs basic arithmetic operations.
    Supports: addition, subtraction, multiplication, and division.
    """
    
    def __init__(self):
        """Initialize the calculator with operation mapping."""
        self.operations = {
            'add': self.add,
            '+': self.add,
            'subtract': self.subtract,
            '-': self.subtract,
            'multiply': self.multiply,
            '*': self.multiply,
            'divide': self.divide,
            '/': self.divide
        }
    
    def add(self, a: float, b: float) -> float:
        """Perform addition: a + b"""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Perform subtraction: a - b"""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Perform multiplication: a * b"""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """
        Perform division: a / b
        Raises ValueError if division by zero is attempted.
        """
        if b == 0:
            raise ValueError("Error: Division by zero is not allowed")
        return a / b
    
    def calculate(self, a: float, b: float, operation: str) -> float:
        """
        Perform calculation based on the operation type.
        
        Args:
            a (float): First number
            b (float): Second number
            operation (str): Type of operation (add, subtract, multiply, divide)
            
        Returns:
            float: Result of the calculation
            
        Raises:
            ValueError: If operation is not supported or division by zero
        """
        operation = operation.lower().strip()
        
        if operation not in self.operations:
            raise ValueError(f"Error: Operation '{operation}' is not supported. "
                           f"Supported operations: add, subtract, multiply, divide")
        
        return self.operations[operation](a, b)


def auto_test_mode():
    """Run automated tests for the calculator."""
    calc = Calculator()
    
    # Test cases
    test_cases = [
        (10.5, 5.5, "add"),
        (20.0, 8.0, "subtract"),
        (4.5, 3.0, "multiply"),
        (15.0, 3.0, "divide"),
        (10.0, 0.0, "divide"),  # Division by zero test
        (5.0, 3.0, "modulo")    # Unsupported operation test
    ]
    
    print("\n" + "="*50)
    print("AUTOMATED TEST MODE")
    print("="*50)
    
    for i, (a, b, operation) in enumerate(test_cases, 1):
        try:
            result = calc.calculate(a, b, operation)
            print(f"Test {i}: {a} {operation} {b} = {result}")
        except ValueError as e:
            print(f"Test {i}: {a} {operation} {b} = {e}")
    
    print("="*50 + "\n")


def interactive_mode():
    """Run calculator in interactive mode with user input."""
    calc = Calculator()
    
    print("\n" + "="*50)
    print("INTERACTIVE CALCULATOR")
    print("="*50)
    print("Operations: add (+), subtract (-), multiply (*), divide (/)")
    print("="*50 + "\n")
    
    while True:
        # Get 1st num
        while True:
            try:
                a_input = input("Enter first number (a): ").strip()
                a = float(a_input)
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.\n")
        
        # Get 2nd num
        while True:
            try:
                b_input = input("Enter second number (b): ").strip()
                b = float(b_input)
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.\n")
        
        # Get operation
        valid_operations = list(calc.operations.keys())
        while True:
            operation = input("Enter operation (add or subtract or multiply or divide or + or - or * or /): ").strip().lower()
            if operation in valid_operations:
                break
            else:
                print("Invalid operation! Please enter one of: add, subtract, multiply, divide (or +, -, *, /)\n")
        
        # Calculate and display result
        try:
            result = calc.calculate(a, b, operation)
            print(f"\nResult: {a} {operation} {b} = {result}")
        except ValueError as e:
            print(f"\n{e}")
        
        print("-"*50)
        while True:
            continue_choice = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
            if continue_choice in ['yes', 'y', '1', 'no', 'n', '0', 'exit', 'quit']:
                break
            print("Please enter 'yes' or 'no'")
        
        if continue_choice in ['no', 'n', '0', 'exit', 'quit']:
            print("\nGetting back to Main Menu!")
            break
        else:
            print() # blank line before next calculation


def main():
    """Main function to run calculator in selected mode."""
    try:
        print("="*50)
        print("CALCULATOR APPLICATION")
        print("="*50)
        
        while True:
            print("\nSelect Mode:")
            print("1. Interactive Mode (User Input)")
            print("2. Auto Test Mode")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1/2/3): ").strip()
            
            if choice == '1':
                interactive_mode()
            elif choice == '2':
                auto_test_mode()
            elif choice == '3':
                print("\nThank you for using the calculator. Goodbye!")
                break
            else:
                print("\nInvalid choice! Please enter 1, 2, or 3.")
    except KeyboardInterrupt:
        print("\n\nCalculator interrupted. Goodbye!")


if __name__ == "__main__":
    main()
