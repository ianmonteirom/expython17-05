"""
2. Dizemos que um número natural é triangular se ele é produto de três números
naturais consecutivos.
Por exemplo:
120 é triangular, pois 4 * 5 * 6 = 120.
2730 é triangular, pois 13 * 14 * 15 = 2730.
Faça uma função que receba um número inteiro e retorne True se for um número
triangular e False, caso contrário.
"""


def triangular(n):
    i1, i2, i3 = 1, 1, 1
    for i1 in range(1, n):
        for i2 in range(i1, n):
            for i3 in range(i2, n):
                if n % i3 == 0 and i3 - i2 == 1 and i3 - i1 == 2:
                    if (i1 * i2 * i3) == n:
                        print(f'{i1} * {i2} * {i3} = {n}')
                        return True
    if (i1 * i2 * i3) != n:
        return False

    """
    d1, d2, d3 = 1, 1, 1
    for i3 in range(1, n+1):
        for i2 in range(1, n+1):
            for i1 in range(1, n+1):
                if n % i1 == 0 and i1 - i2 == -1:
                    d1 = i1
                if n % i2 == 0 and i2 - i3 == -1:
                    d2 = i2
                if n % i3 == 0 and i3 - i2 == 1:
                    d3 = i3
                if d1 * d2 * d3 == n:
                    break
                print(f'{d1}, {d2}, {d3}')
    print(d1, d2, d3)

    if d1 * d2 * d3 == n:
        return True
    else:
        return False
"""


num = int(input('Seu número: '))

print(triangular(num))
