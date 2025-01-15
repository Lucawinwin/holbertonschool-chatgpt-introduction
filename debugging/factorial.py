#!/usr/bin/python3
import sys

def factorielle(n):
    resultat = 1
    while n > 1:
        resultat *= n
        n -= 1  # Décrémenter n pour éviter une boucle infinie
    return resultat

# Vérifier qu'un argument a été passé
if len(sys.argv) != 2:
    print("Veuillez fournir un nombre en argument.")
    sys.exit(1)

# Calculer et afficher la factorielle
n = int(sys.argv[1])
f = factorielle(n)
print(f)

