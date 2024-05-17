"""
1. Crie uma função que receba três números como parâmetros, e retorne True se a
soma de quaisquer pares de números gera a soma do terceiro número. Caso
contrário retorne False.
"""


def somaNumeros(n1, n2, n3):
    if n1 + n2 == n3 or n2 + n3 == n1 or n1 + n3 == n2:
        return True
    else:
        return False


num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

print(somaNumeros(num1, num2, num3))
