#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:  # Cas où n est égal à 0
        return 1
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) != 2:
    print("Veuillez fournir un argument.")
    sys.exit(1)

try:
    f = factorial(int(sys.argv[1]))
    print(f)
except ValueError:
    print("Veuillez entrer un nombre entier valide.")
