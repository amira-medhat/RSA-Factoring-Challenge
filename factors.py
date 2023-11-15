#!/usr/bin/python3
import sys

def factorize(n):
    # Find two factors of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    # If n is prime, return n as one of the factors
    return n, 1

def main(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Convert the line to an integer
                n = int(line)
                # Factorize the number
                factor1, factor2 = factorize(n)
                # Print the factorization
                print(f"{n}={factor2}*{factor1}")
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
