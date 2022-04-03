lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = ["Arroz", "Feijao", "Miojo", "Coco", "Galinha", "Gelo", "Uva", "Pera"]
lista3 = ["R$ 3,50", "R$ 3,50", "R$ 3,50", "R$ 3,50",
          "R$ 3,50", "R$ 3,50", "R$ 3,50", "R$ 3,50"]

# A função zip une todos os valores
for indice, item, valor in zip(lista1, lista2, lista3):
    print(indice, item, valor)
