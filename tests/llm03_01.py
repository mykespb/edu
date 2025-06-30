import math
import random

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
    Main function to generate random coefficients and find the roots of the quadratic equation.
    """
    for i in range(10):
        print(f"--- Run {i+1}/10 ---")
        a = random.uniform(-10.0, 10.0)
        b = random.uniform(-10.0, 10.0)
        c = random.uniform(-10.0, 10.0)

        print(f"Solving for the equation: {a:.2f}x^2 + {b:+.2f}x + {c:+.2f} = 0")

        if abs(a) < 1e-9:  # Treat as a linear equation
            if abs(b) < 1e-9:
                if abs(c) < 1e-9:
                    print("The equation is 0 = 0, which is true for all x.")
                else:
                    print("The equation is a contradiction, no solution.")
            else:
                root = -c / b
                print(f"This is a linear equation. The root is: {root}")
            continue

        roots = find_roots(a, b, c)

        if not roots:
            print("No real roots were found in the search range.")
        else:
            print(f"Found {len(roots)} root(s):")
            for r in sorted(roots):
                print(f"Root: {r:.6f}")
        print()

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


# myke@mykex:~/pro/edu/tests$ python llm03_01.py
# --- Run 1/10 ---
# Solving for the equation: -7.00x^2 + +6.90x + -0.28 = 0
# Found 2 root(s):
# Root: 0.042192
# Root: 0.944552

# --- Run 2/10 ---
# Solving for the equation: -3.81x^2 + -6.71x + +6.71 = 0
# Found 2 root(s):
# Root: -2.474725
# Root: 0.712268

# --- Run 3/10 ---
# Solving for the equation: -9.27x^2 + +3.73x + +3.92 = 0
# Found 2 root(s):
# Root: -0.479461
# Root: 0.882101

# --- Run 4/10 ---
# Solving for the equation: 2.63x^2 + -0.38x + -7.40 = 0
# Found 2 root(s):
# Root: -1.608303
# Root: 1.753457

# --- Run 5/10 ---
# Solving for the equation: 5.95x^2 + -6.30x + +9.78 = 0
# No real roots were found in the search range.

# --- Run 6/10 ---
# Solving for the equation: 9.18x^2 + +8.82x + +8.13 = 0
# No real roots were found in the search range.

# --- Run 7/10 ---
# Solving for the equation: 6.68x^2 + -1.22x + +0.96 = 0
# No real roots were found in the search range.

# --- Run 8/10 ---
# Solving for the equation: 4.26x^2 + +9.55x + +1.79 = 0
# Found 2 root(s):
# Root: -2.033025
# Root: -0.206577

# --- Run 9/10 ---
# Solving for the equation: -2.91x^2 + -3.72x + -8.39 = 0
# No real roots were found in the search range.

# --- Run 10/10 ---
# Solving for the equation: 3.50x^2 + +0.17x + -0.66 = 0
# Found 2 root(s):
# Root: -0.459374
# Root: 0.411979
