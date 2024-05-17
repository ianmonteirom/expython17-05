"""
5. Faça uma função que recebe um número inteiro e retorna a quantidade de dígitos
desse número
"""


def tamanho(n):
    nstr = str(n)
    return len(nstr)


num = int(input('Digite um número inteiro: '))
print(f'{num} possui {tamanho(num)} dígitos')
