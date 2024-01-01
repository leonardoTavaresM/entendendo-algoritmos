def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9]
print(busca_binaria(minha_lista, 3))  # Retorna 1 (índice do item na lista)

lista = ['a','b','c']

# """A busca binária é um algoritmo eficiente que divide repetidamente 
# o espaço de busca pela metade até encontrar o elemento desejado.
# A complexidade de tempo da busca binária é O(log n),
# onde "n" é o número de elementos na lista ordenada."""