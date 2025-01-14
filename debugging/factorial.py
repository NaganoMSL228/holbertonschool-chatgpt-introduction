#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        return None  # Le factoriel n'est pas défini pour les nombres négatifs
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if len(sys.argv) > 1:
    try:
        n = int(sys.argv[1])
        f = factorial(n)
        if f is None:
            print("Le factoriel n'est pas défini pour les nombres négatifs.")
        else:
            print(f)
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")
else:
    print("Veuillez fournir un argument numérique.")
