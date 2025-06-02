#!/usr/bin/env python
# prime factors
# Mikhail Kolodin
# 2025-06-01 2025-06-02

# ~ Write a program in python which takes a positive integer as an argument and returns the number of prime factors of this integer. You can write and use otyer subroutines (eg checking if number is prime) to help you with the miain task.

# ~ Certainly! Below is a Python program that takes a positive integer as an argument and returns the number of prime factors of that integer. The program includes a helper function to check if a number is prime.

# ~ python
# ~ 42 lines
# ~ Click to close
# ~ def is_prime(n):
# ~ """Check if a number is prime."""
# ~ ...
# ~ Explanation:
# ~ is_prime(n): This function checks if a number 
 # ~ is prime. It handles small numbers and uses trial division for larger numbers.
# ~ prime_factors_count(n): This function counts the number of prime factors of 
# ~ . It first counts the factors of 2, then checks for odd factors up to the square root of 
# ~ . If 
 # ~ is still greater than 2 after the loop, it means 
 # ~ itself is a prime factor.
# ~ The program prompts the user to enter a positive integer and then prints the number of prime factors.
# ~ You can run this program in a Python environment, and it will return the number of prime factors for any positive integer you input.

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors_count(n):
    """Return the number of prime factors of a positive integer n."""
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    count = 0
    # Check for number of 2s that divide n
    while n % 2 == 0:
        count += 1
        n //= 2
    
    # n must be odd at this point, so we can skip even numbers
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            count += 1
            n //= i
    
    # This condition is to check if n is a prime number greater than 2
    if n > 2:
        count += 1
    
    return count

# Example usage
def test1():
    number = int(input("Enter a positive integer: "))
    print(f"The number of prime factors of {number} is: {prime_factors_count(number)}")

# ================================================

def get_primes(limit: int) -> list[int]:
    """Get primes list for limit"""

    table = []

    for test in range(2, limit+1):
        for tester in range(2, test):
            if test % tester == 0:
                break
        else:
            table.append(test)

    return table

# ~ print(get_primes(100))


def num_pf(num: int) -> int:
    """calculate number of prime factors for given number"""

    if num < 2:
        return 0    # Primes are not defined for numbers below 2

    # table of primes
    top = get_primes(num)

    # counter of prime factors
    cpf = 0

    # main loop: divide num by all known primes and count successful cases;
    # there may be multiple cases for each prime.
    while num > 1:
        for d in top:
            if num % d == 0:
                cpf += 1
                num //= d

    return cpf


def num_pf_verbose(num: int) -> int:
    """calculate number of prime factors for given number and show the full list"""

    print(f"We got {num} to study:")

    if num < 2:
        return 0    # Primes are not defined for numbers below 2

    # table of primes
    top = get_primes(num)

    # counter of prime factors
    cpf = 0

    # list of primes factors
    lopf = []

    # main loop: divide num by all known primes and count successful cases;
    # there may be multiple cases for each prime.
    while num > 1:
        for d in top:
            if num % d == 0:
                cpf += 1
                num //= d
                lopf.append(d)

    print("primes factors:", lopf)
    print("counter of primes factors:", cpf)

    return cpf


def test(limit: int) -> None:
    """Make tests"""

    for num in range(1, limit+1):
        print(f"For number {num} we have {num_pf(num)} prime factor(s).")


def test_verbose(limit: int) -> None:
    """Make tests verbousely"""

    for num in range(1, limit+1):
        print(f"For number {num} we have {num_pf_verbose(num)} prime factor(s).")


test(50)

test_verbose(20)


# ~ For number 1 we have 0 prime factor(s).
# ~ For number 2 we have 1 prime factor(s).
# ~ For number 3 we have 1 prime factor(s).
# ~ For number 4 we have 2 prime factor(s).
# ~ For number 5 we have 1 prime factor(s).
# ~ For number 6 we have 2 prime factor(s).
# ~ For number 7 we have 1 prime factor(s).
# ~ For number 8 we have 3 prime factor(s).
# ~ For number 9 we have 2 prime factor(s).
# ~ For number 10 we have 2 prime factor(s).
# ~ For number 11 we have 1 prime factor(s).
# ~ For number 12 we have 3 prime factor(s).
# ~ For number 13 we have 1 prime factor(s).
# ~ For number 14 we have 2 prime factor(s).
# ~ For number 15 we have 2 prime factor(s).
# ~ For number 16 we have 4 prime factor(s).
# ~ For number 17 we have 1 prime factor(s).
# ~ For number 18 we have 3 prime factor(s).
# ~ For number 19 we have 1 prime factor(s).
# ~ For number 20 we have 3 prime factor(s).
# ~ For number 21 we have 2 prime factor(s).
# ~ For number 22 we have 2 prime factor(s).
# ~ For number 23 we have 1 prime factor(s).
# ~ For number 24 we have 4 prime factor(s).
# ~ For number 25 we have 2 prime factor(s).
# ~ For number 26 we have 2 prime factor(s).
# ~ For number 27 we have 3 prime factor(s).
# ~ For number 28 we have 3 prime factor(s).
# ~ For number 29 we have 1 prime factor(s).
# ~ For number 30 we have 3 prime factor(s).
# ~ For number 31 we have 1 prime factor(s).
# ~ For number 32 we have 5 prime factor(s).
# ~ For number 33 we have 2 prime factor(s).
# ~ For number 34 we have 2 prime factor(s).
# ~ For number 35 we have 2 prime factor(s).
# ~ For number 36 we have 4 prime factor(s).
# ~ For number 37 we have 1 prime factor(s).
# ~ For number 38 we have 2 prime factor(s).
# ~ For number 39 we have 2 prime factor(s).
# ~ For number 40 we have 4 prime factor(s).
# ~ For number 41 we have 1 prime factor(s).
# ~ For number 42 we have 3 prime factor(s).
# ~ For number 43 we have 1 prime factor(s).
# ~ For number 44 we have 3 prime factor(s).
# ~ For number 45 we have 3 prime factor(s).
# ~ For number 46 we have 2 prime factor(s).
# ~ For number 47 we have 1 prime factor(s).
# ~ For number 48 we have 5 prime factor(s).
# ~ For number 49 we have 2 prime factor(s).
# ~ For number 50 we have 3 prime factor(s).


# ~ We got 1 to study:
# ~ For number 1 we have 0 prime factor(s).
# ~ We got 2 to study:
# ~ primes factors: [2]
# ~ counter of primes factors: 1
# ~ For number 2 we have 1 prime factor(s).
# ~ We got 3 to study:
# ~ primes factors: [3]
# ~ counter of primes factors: 1
# ~ For number 3 we have 1 prime factor(s).
# ~ We got 4 to study:
# ~ primes factors: [2, 2]
# ~ counter of primes factors: 2
# ~ For number 4 we have 2 prime factor(s).
# ~ We got 5 to study:
# ~ primes factors: [5]
# ~ counter of primes factors: 1
# ~ For number 5 we have 1 prime factor(s).
# ~ We got 6 to study:
# ~ primes factors: [2, 3]
# ~ counter of primes factors: 2
# ~ For number 6 we have 2 prime factor(s).
# ~ We got 7 to study:
# ~ primes factors: [7]
# ~ counter of primes factors: 1
# ~ For number 7 we have 1 prime factor(s).
# ~ We got 8 to study:
# ~ primes factors: [2, 2, 2]
# ~ counter of primes factors: 3
# ~ For number 8 we have 3 prime factor(s).
# ~ We got 9 to study:
# ~ primes factors: [3, 3]
# ~ counter of primes factors: 2
# ~ For number 9 we have 2 prime factor(s).
# ~ We got 10 to study:
# ~ primes factors: [2, 5]
# ~ counter of primes factors: 2
# ~ For number 10 we have 2 prime factor(s).
# ~ We got 11 to study:
# ~ primes factors: [11]
# ~ counter of primes factors: 1
# ~ For number 11 we have 1 prime factor(s).
# ~ We got 12 to study:
# ~ primes factors: [2, 3, 2]
# ~ counter of primes factors: 3
# ~ For number 12 we have 3 prime factor(s).
# ~ We got 13 to study:
# ~ primes factors: [13]
# ~ counter of primes factors: 1
# ~ For number 13 we have 1 prime factor(s).
# ~ We got 14 to study:
# ~ primes factors: [2, 7]
# ~ counter of primes factors: 2
# ~ For number 14 we have 2 prime factor(s).
# ~ We got 15 to study:
# ~ primes factors: [3, 5]
# ~ counter of primes factors: 2
# ~ For number 15 we have 2 prime factor(s).
# ~ We got 16 to study:
# ~ primes factors: [2, 2, 2, 2]
# ~ counter of primes factors: 4
# ~ For number 16 we have 4 prime factor(s).
# ~ We got 17 to study:
# ~ primes factors: [17]
# ~ counter of primes factors: 1
# ~ For number 17 we have 1 prime factor(s).
# ~ We got 18 to study:
# ~ primes factors: [2, 3, 3]
# ~ counter of primes factors: 3
# ~ For number 18 we have 3 prime factor(s).
# ~ We got 19 to study:
# ~ primes factors: [19]
# ~ counter of primes factors: 1
# ~ For number 19 we have 1 prime factor(s).
# ~ We got 20 to study:
# ~ primes factors: [2, 5, 2]
# ~ counter of primes factors: 3
# ~ For number 20 we have 3 prime factor(s).
