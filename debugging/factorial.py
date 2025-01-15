#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Décrémente n à chaque itération
    return result

if len(sys.argv) > 1:
    try:
        n = int(sys.argv[1])
        if n < 0:
            print("Le factoriel n'est pas défini pour les nombres négatifs.")
        else:
            f = factorial(n)
            print(f)
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")
else:
    print("Veuillez fournir un argument numérique.")
