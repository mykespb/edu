"""
This program defines a function to draw a square of stars of a given size.
The size is passed as a parameter to the function, which then prints the square.
"""

def draw_square(size):
    """
    Draws a square of stars of a given size.
    
    Args:
        size (int): The size of the square (number of rows and columns).
    """
    if not isinstance(size, int) or size <= 0:
        print("Error: Size must be a positive integer.")
        return
    
    for _ in range(size):
        print('* ' * size)

def main():
    """
    Main function to demonstrate the draw_square function.
    It prompts the user for the size of the square and then draws it.
    """
    try:
        size_input = input("Enter the size of the square: ")
        size = int(size_input)
        print(f"\nDrawing a square of size {size}x{size}:\n")
        draw_square(size)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the size.")

if __name__ == "__main__":
    main()


# Enter the size of the square: 5

# Drawing a square of size 5x5:

# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 