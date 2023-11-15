#!/usr/bin/python3
import sys
import time

def is_prime(num):
    # Check if a number is prime using trial division
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_factors(n):
    # Find prime factors of n using trial division
    factors = []
    for i in range(2, n + 1):
        while n % i == 0 and is_prime(i):
            factors.append(i)
            n //= i
        if n == 1:
            break
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

                # Find prime factors of the number
                prime_factors = find_prime_factors(n)

                if len(prime_factors) == 2:
                    p, q = prime_factors
                    print(f"{n}={p}*{q}")
                else:
                    print(f"Error: Unable to find two prime factors for {n}")
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
