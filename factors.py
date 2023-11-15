#!/usr/bin/python3
import sys
import time

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
        
        factors.extend([factor, n] if n != 1 else [factor])

    return factors

def main(file_path):
    start_time = time.time()
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Convert the line to an integer
                n = int(line)
                
                # Check time limit
                if time.time() - start_time > 5:
                    print("Time limit exceeded")
                    exit()
                
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
