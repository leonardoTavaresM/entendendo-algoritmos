def buscaMenor(arr):
  menor = arr[0] #armazena o menor valor
  menor_indice = 0 # armazena o indice do menor valor
  for i in range(1,len(arr)):
    if arr[i] < menor:
      menor = arr[i]
      menor_indice = i
  return menor_indice


def ordenacaoPorSelecao(arr):
  novoArr = []
  for i in range(len(arr)):
    menor = buscaMenor(arr) # Encontra o menor elemento do array e adiciona ao novo array
    novoArr.append(arr.pop(menor))
  return novoArr

# Exemplo de uso do algoritmo de ordenação por seleção
arr = [5, 3, 6, 2, 10]
arr_ordenado = ordenacaoPorSelecao(arr)
print('Ordenação por seleção:', arr_ordenado)


#complexidade de tempo do selection sort é O(n^2), onde "n" é o número de elementos na lista.
