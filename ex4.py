"""
4. Crie uma função chamada bhaskara que receba 3 valores (a, b, c) e calcule as 
raízes da fórmula de Bhāskara. Faça um teste com bhaskara(1, -4, -5) e a função 
deve exibir as raízes: 5.0 e -1.0.
"""

from math import sqrt


def bhaskara(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    x1 = (-b + sqrt(delta)) / 2 * a
    x2 = (-b - sqrt(delta)) / 2 * a
    return x1, x2


v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))

print(bhaskara(v1, v2, v3))
