lista = ["galinha", "pato", "gato"]

"""for i in range(len(lista)):  # range cria o vetor len mede o tamanho da lista
    print(i, lista[i])"""

for i, nome in enumerate(lista):  # funcao cria vetor e mede tamanho ao mesmo tempo
    print(i, nome)
