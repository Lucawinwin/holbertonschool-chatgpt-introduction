def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Décrémenter n à chaque itération
    return result
