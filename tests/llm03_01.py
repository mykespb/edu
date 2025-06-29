import math

"""
This program finds the roots of a quadratic equation ax^2 + bx + c = 0
using the bisection method (method of half division).
The coefficients a, b, and c are provided by the user.
"""

def quadratic_function(x, a, b, c):
    """
    Represents the quadratic equation f(x) = ax^2 + bx + c.
    
    Args:
        x (float): The value at which to evaluate the function.
        a (float): The coefficient of the x^2 term.
        b (float): The coefficient of the x term.
        c (float): The constant term.
    
    Returns:
        float: The value of the function at x.
    """
    return a * x**2 + b * x + c

def bisection_method(a, b, c, x1, x2, tolerance=1e-7, max_iterations=100):
    """
    Finds a root of the quadratic equation in the interval [x1, x2]
    using the bisection method.
    
    Args:
        a (float): The coefficient of the x^2 term.
        b (float): The coefficient of the x term.
        c (float): The constant term.
        x1 (float): The start of the interval.
        x2 (float): The end of the interval.
        tolerance (float): The desired accuracy of the root.
        max_iterations (int): The maximum number of iterations to perform.
    
    Returns:
        float or None: The root of the equation, or None if a root is not found.
    """
    f1 = quadratic_function(x1, a, b, c)
    f2 = quadratic_function(x2, a, b, c)

    if f1 * f2 >= 0:
        return None  # No root in this interval or multiple roots

    for _ in range(max_iterations):
        midpoint = (x1 + x2) / 2
        f_mid = quadratic_function(midpoint, a, b, c)

        if abs(f_mid) < tolerance:
            return midpoint

        if f1 * f_mid < 0:
            x2 = midpoint
            f2 = f_mid
        else:
            x1 = midpoint
            f1 = f_mid
            
    return (x1 + x2) / 2

def find_roots(a, b, c):
    """
    Finds the roots of the quadratic equation by searching for intervals
    and then applying the bisection method.
    
    Args:
        a (float): The coefficient of the x^2 term.
        b (float): The coefficient of the x term.
        c (float): The constant term.
    
    Returns:
        list: A list of found roots.
    """
    roots = []
    # Search for roots in a wide range
    search_range = 1000
    step = 0.1
    x = -search_range
    
    while x < search_range:
        x1 = x
        x2 = x + step
        root = bisection_method(a, b, c, x1, x2)
        if root is not None and not any(abs(r - root) < 1e-5 for r in roots):
            roots.append(root)
        x += step
        
    # Special check for vertex if it's a root
    if a != 0:
        vertex_x = -b / (2 * a)
        if abs(quadratic_function(vertex_x, a, b, c)) < 1e-7:
            if not any(abs(r - vertex_x) < 1e-5 for r in roots):
                roots.append(vertex_x)

    return roots

def main():
    """
    Main function to get user input and find the roots of the quadratic equation.
    """
    try:
        print("Enter the coefficients for the quadratic equation (ax^2 + bx + c = 0):")
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))

        if a == 0:
            if b == 0:
                if c == 0:
                    print("The equation is 0 = 0, which is true for all x.")
                else:
                    print("The equation is a contradiction, no solution.")
            else:
                root = -c / b
                print(f"This is a linear equation. The root is: {root}")
            return

        roots = find_roots(a, b, c)

        if not roots:
            print("No real roots were found in the search range.")
        else:
            print(f"Found {len(roots)} root(s):")
            for r in sorted(roots):
                print(f"Root: {r:.6f}")

    except ValueError:
        print("Invalid input. Please enter valid numbers for the coefficients.")

if __name__ == "__main__":
    main()



# myke@mykex:~/pro/edu/tests$ python llm03_01.py
# Enter the coefficients for the quadratic equation (ax^2 + bx + c = 0):
# Enter a: 1
# Enter b: -5
# Enter c: -12
# Found 2 root(s):
# Root: -1.772002
# Root: 6.772002
