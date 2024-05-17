"""
2. Dizemos que um número natural é triangular se ele é produto de três números
naturais consecutivos.
Por exemplo:
120 é triangular, pois 4 * 5 * 6 = 120.
2730 é triangular, pois 13 * 14 * 15 = 2730.
Faça uma função que receba um número inteiro e retorne True se for um número
triangular e False, caso contrário.
"""

from math import factorial

def triangular(n):
    d1, d2, d3 = 1, 1, 1
    for i1 in range(1, n+1):
        for i2 in range(1, n+1):
            for i3 in range(1, n+1):
                if n % i1 == 0:
                    d1 = i1
                if n % i2 == 0:
                    d2 = i2
                if n % i3 == 0:
                    d3 = i3
                if d1 * d2 * d3 == n:
                    break
                print(f'{d1}, {d2}, {d3}')
    print(d1, d2, d3)

    if d1 * d2 * d3 == n:
        return True
    else:
        return False



num = int(input('Seu número: '))

print(triangular(num))
