from typing import Tuple


lista = [1, 44, 3, 4, 20, 50]
lista_animal = ['gato', 'cachorro', 'galinha', 'pato']

""" print(lista) #Imprime a lista
print(lista_animal[1]) #Imprime a lista e seta o indice 
print(min(lista)) # imprime o menor valor da lista  
print(max(lista)) # imprime o maior valor da lista
print(sum(lista)) # imprime o valor da soma de toda a lista

if 'pato' in lista_animal: # a condicional procura se tem um pato na lista
    print('Existe um Pato') 
else:
    print('Não Existe na lista')
    lista_animal.append('pato') # adiciona o elemento não existente na lista
    print(lista_animal)

lista_animal.pop() #remove o ultimo elemento da lista
print(lista_animal) """

""" lista.sort()
lista_animal.sort()

print(lista)
print(lista_animal) """

""" lista_animal[0] = 'Macaco'
print(lista_animal) """

tuple = (1, 10, 20, 30)
print(tuple)
print(len(tuple))# o len retorna a quantidade de elementos que tem no tuple 
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))



