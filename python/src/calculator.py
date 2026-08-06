"""
Basic calculator functionality.
"""

def add(a: float, b: float) -> float:
    """Adds two numbers together and returns the sum."""
    return a + b


def main():
    """Main entry point. """
    num1 = 5
    num2 = 7
    result = add(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()
