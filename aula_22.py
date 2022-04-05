from functools import reduce


def soma(x, y):
    return x + y


lista = [1, 3, 4, 5]

soma = reduce(soma, lista)  # Soma o valor de todos os itens da lista
print(soma)
