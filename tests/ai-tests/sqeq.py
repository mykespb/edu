#!/usr/bin/env python3
"""
Square Equations Solver - Automated Testing Version
Solve quadratic equations and test automatically

Usage: python sqeq.py [--test TESTS] where TESTS is optional number of tests (default: 10)
"""

import cmath
import random
from typing import Tuple, List

def solve_quadratic(a: float, b: float, c: float) -> Tuple[complex, complex]:
    """
    Solve quadratic equation: a*x² + b*x - c = 0
    
    Returns two solutions (potentially complex if discriminant < 0)
    """
    if a == 0:
        raise ValueError("Coefficient 'a' must not be zero")
    
    discriminant = (b**2) - (4*a*(-c))
    sol1 = (-b-cmath.sqrt(discriminant))/(2*a)
    sol2 = (-b+cmath.sqrt(discriminant))/(2*a)
    return sol1, sol2

import re

def parse_equation(equation: str) -> Tuple[float, float, float]:
    """
    Parse 'ax^2+bx=c' format into (a, b, c) floats
    Handles cases like x²+x=1 as well as 2x²+3x=-5 or 2x²=x+5
    """
    if not equation or "=" not in equation:
        raise ValueError("Missing '=' sign")
    
    left_part, right_term = [p.strip() for p in equation.split("=")]
    
    # Find coefficients using regex
    a_coeff = float(re.search(r'^([\d.]+)x\^2', left_part).group(1)) if re.match(r'[\d.]+x\^2', left_part) else (float(1)) if 'x^2' in left_part else None
    
    b_coeff = float(re.search(r'([+-]?[0-9.]*?)x$', left_part).group(1).replace('+', '')) if re.search(r'([+-]?[0-9.]*?)x$', left_part) else 0.0
    c_coeff = float(right_term.strip())
    
    return a_coeff, b_coeff, c_coeff

def generate_test_case(use_complex: bool = False) -> Tuple[str, List[complex]]:
    """
    Generate a random quadratic test case with known solutions
    
    Returns: (equation_str, [expected_root1, expected_root2])
    """
    # Randomly decide if we want a specific root or just coefficients
    if use_complex and random.random() > 0.5:
        # Create complex roots with non-real part to ensure we test cmath
        root1 = complex(random.uniform(-2, 2), random.uniform(0.5, 1.5))
        root2 = complex(random.uniform(-2, 2), -random.uniform(0.5, 1.5))
    else:
        # Use real roots from interval [-1.5, 3.0]
        root1 = random.uniform(-1.5, 3.0)
        root2 = random.uniform(-1.5, 3.0)
    
    # Quadratic formula: x² - (r1+r2)x + r1*r2 = 0
    a = 1.0
    b = -(root1 + root2)
    c = root1 * root2
    
    b_sign = "+" if b >= 0 else ""
    equation = f"{a}x^2 {b:+} x={c}"
    equation = equation.replace("++", "+").replace("--", "-")
    return equation, [root1, root2]

def run_tests(num_tests: int = 10) -> None:
    """
    Run automated test suite for quadratic solver
    
    Prints summary statistics and any failures
    """
    passed = 0
    failed = 0
    errors = []
    
    # Generate tests: mix of real and complex cases
    use_complex_tests = bool(random.getrandbits(1))
    
    print(f"Running {num_tests} quadratic equation tests...")
    for test_num in range(num_tests):
        try:
            equation, expected_roots = generate_test_case(use_complex_tests)
            a, b, c = parse_equation(equation)
            actual_roots = solve_quadratic(a, b, c)
            
            # Check if roots match (allowing for rounding errors)
            root1_tolerance = abs(actual_roots[0] - expected_roots[0]) < 0.01
            root2_tolerance = abs(actual_roots[1] - expected_roots[1]) < 0.01
            
            if root1_tolerance and root2_tolerance:
                passed += 1
            else:
                failed += 1
                errors.append({
                    'equation': equation,
                    'expected': expected_roots,
                    'actual': actual_roots
                })
        except Exception as e:
            failed += 1
            error_info = f"Error processing '{equation}': {str(e)}"
            print(error_info)
    
    # Print results summary
    print(f"[32mResults: {passed}/{num_tests} tests passed\u001b[0m")
    if failed > 0:
        print(f"Failed on:\n{chr(10).join(errors)}")

if __name__ == "__main__":
    # Allow command line override for test count
    try:
        import sys
        num_tests = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].startswith('--test=') else 10
        run_tests(num_tests)
    except IndexError:
        # Default to 10 tests as requested
        run_tests(10)