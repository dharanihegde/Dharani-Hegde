"""
Problem-3: Pattern-based Odd Number Series Generator
Generate odd numbers based on a specific pattern where even inputs 
produce the same output as the previous odd input.
"""

def generate_pattern_odd_series(a: int) -> list:
    """
    Generate odd numbers based on the pattern:
    - If 'a' is odd: generate 'a' odd numbers
    - If 'a' is even: generate 'a-1' odd numbers
    
    Args:
        a (int): Input value
        
    Returns:
        list: List of odd numbers following the pattern
        
    Examples:
        a = 1 -> [1]
        a = 2 -> [1]
        a = 3 -> [1, 3, 5]
        a = 4 -> [1, 3, 5]
        a = 5 -> [1, 3, 5, 7, 9]
        a = 6 -> [1, 3, 5, 7, 9]
    """
    if a <= 0:
        return []
    
    # If 'a' is even, use a-1; if odd, use a
    count = a if a % 2 == 1 else a - 1
    
    return [2 * i - 1 for i in range(1, count + 1)]


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
    """Run the pattern-based odd series generator."""
    print("\n" + "="*50)
    print("PATTERN-BASED ODD NUMBER SERIES GENERATOR")
    print("="*50)
    print("Pattern: Even inputs give same output as previous odd")
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
        
        odd_numbers = generate_pattern_odd_series(a)
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
            print()  # blank line before next calculation


if __name__ == "__main__":
    main()
