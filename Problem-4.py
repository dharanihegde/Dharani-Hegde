"""
Problem-4: Multiple Counter Dictionary
Count how many numbers in a list are multiples of each number from 1 to 9.
"""

def count_multiples(numbers: list) -> dict:
    """
    Count how many numbers in the list are multiples of each number from 1 to 9.
    
    Args:
        numbers (list): List of integers to analyze
        
    Returns:
        dict: Dictionary with keys 1-9 and count of multiples as values
        
    Example:
        Input: [1,2,8,9,12,46,76,82,15,20,30]
        Output: {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
    """
    multiple_counts = {i: 0 for i in range(1, 10)}
    

    for div in range(1, 10):
        for num in numbers:
            if num % div == 0:
                multiple_counts[div] += 1
    
    return multiple_counts


def parse_input(input_string: str) -> list:
    """
    Parse input string to extract list of integers.
    Handles various input formats.
    
    Args:
        input_string (str): String containing numbers
        
    Returns:
        list: List of integers
    """
    input_string = input_string.strip()
    input_string = input_string.replace('[', '').replace(']', '')
    
    try:
        numbers = [int(x.strip()) for x in input_string.split(',') if x.strip()]
        return numbers
    except ValueError:
        return []


def format_output(result: dict) -> str:
    """
    Format the dictionary result as a string.
    
    Args:
        result (dict): Dictionary with multiple counts
        
    Returns:
        str: Formatted string representation
    """
    items = [f"{k}: {v}" for k, v in result.items()]
    return "{" + ", ".join(items) + "}"


def main():
    """Run the multiple counter program."""
    print("\n" + "="*50)
    print("MULTIPLE COUNTER DICTIONARY")
    print("="*50)
    print("Count multiples of 1-9 in a list of numbers")
    print("="*50 + "\n")
    
    print("Example input formats:")
    print("  - 1,2,8,9,12,46,76,82,15,20,30")
    print("  - [1,2,8,9,12,46,76,82,15,20,30]")
    print()
    
    while True:
        while True:
            user_input = input("Enter list of numbers (comma-separated): ").strip()
            if not user_input:
                print("Please enter at least one number.\n")
                continue
                
            numbers = parse_input(user_input)
            if not numbers:
                print("Invalid input! Please enter comma-separated integers.\n")
                continue
            break
        
        result = count_multiples(numbers)
        
        print(f"\nInput: {numbers}")
        print(f"Output: {format_output(result)}")
        
        print("-"*50)
        
        while True:
            continue_choice = input("\nAnalyze another list? (yes/no): ").strip().lower()
            if continue_choice in ['yes', 'y', '1', 'no', 'n', '0', 'exit', 'quit']:
                break
            print("Please enter 'yes' or 'no'")
        
        if continue_choice in ['no', 'n', '0', 'exit', 'quit']:
            print("\nGoodbye!")
            break
        else:
            print() # blank line before next input


if __name__ == "__main__":
    main()
