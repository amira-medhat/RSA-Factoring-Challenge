#!/usr/bin/python3
import sys

def pollards_rho(n):
    # Pollard's rho algorithm for factorization
    x = 2
    y = 2
    d = 1

    f = lambda x: (x**2 + 1) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    return d

def gcd(a, b):
    # Euclidean algorithm for calculating the greatest common divisor
    while b:
        a, b = b, a % b
    return a

def factorize(n):
    # Factorization using Pollard's rho algorithm
    factors = []
    
    while n > 1:
        # Use Pollard's rho to find a non-trivial factor
        factor = pollards_rho(n)
        
        # Divide n by the factor
        n //= factor
        
        factors.append(factor)

    return factors

def main(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Convert the line to an integer
                n = int(line)
                # Factorize the number
                factors = factorize(n)
                # Print the factorization
                print(f"{n}={'*'.join(map(str, factors))}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
