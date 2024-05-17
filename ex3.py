"""
3. Em um jogo de dados, pode ser sorteado qualquer número entre 1 e 6. Faça uma
função que simule 1 milhão de lançamentos de dados e mostre quantas vezes cada
número foi sorteado.
"""

from random import randint


def sorteioDados():
    jogadas = []
    for j in range(1000000):
        jogadas.append(randint(1, 6))
    for i in range(1, 6+1):
        print(f'O número {i} foi sorteado {jogadas.count(i)} vezes')


sorteioDados()
