"""
Problem-2: Odd Number Series Generator
Generate the first 'a' odd numbers based on the input.
"""

def generate_odd_series(a: int) -> list:
    """
    Generate the first 'a' odd numbers.
    
    Args:
        a (int): Number of odd numbers to generate
        
    Returns:
        list: List containing the first 'a' odd numbers
        
    Examples:
        a = 1 -> [1]
        a = 2 -> [1, 3]
        a = 3 -> [1, 3, 5]
        a = 4 -> [1, 3, 5, 7]
    """
    if a <= 0:
        return []
    
    return [2 * i - 1 for i in range(1, a + 1)]


def format_output(numbers: list) -> str:
    """
    Format the list of numbers as a comma-separated string.
    
    Args:
        numbers (list): List of numbers to format
        
    Returns:
        str: Comma-separated string representation
    """
    if not numbers:
        return "No output (a must be positive)"
    
    return ", ".join(map(str, numbers))


def main():
    """Run the program in interactive mode with user input."""
    print("\n" + "="*50)
    print("ODD NUMBER SERIES GENERATOR")
    print("="*50)
    print("This program generates the first 'a' odd numbers.")
    print("="*50 + "\n")
    
    while True:
        while True:
            try:
                user_input = input("Enter value of 'a' (positive integer): ").strip()
                a = int(user_input)
                if a < 0:
                    print("Please enter a positive integer (0 or greater).\n")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.\n")
        
        odd_numbers = generate_odd_series(a)
        output = format_output(odd_numbers)
        
        print(f"\nInput a = {a}")
        print(f"Output: {output}")
        print("-"*50)
        
        while True:
            continue_choice = input("\nGenerate another series? (yes/no): ").strip().lower()
            if continue_choice in ['yes', 'y', '1', 'no', 'n', '0', 'exit', 'quit']:
                break
            print("Please enter 'yes' or 'no'")
        
        if continue_choice in ['no', 'n', '0', 'exit', 'quit']:
            print("\nGoodbye!")
            break
        else:
            print()  # Blank line before next calculation


if __name__ == "__main__":
    main()
    