"""
Main entry point for the sample application.
"""

from src.utils.calculator import add

def main() -> None:
    """
    Main function to demonstrate import and usage.
    """
    x, y = 10, 5
    result = add(x, y)
    print(f"Welcome to my reference guide demo!")
    print(f"Calculation result: {x} + {y} = {result}")

if __name__ == "__main__":
    main()
