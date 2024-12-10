# A ordenação por seleção é um algoritmo bom, mas não é muito rápido. O Quicksort é um algoritmo de ordenação mais rápido, que tem tempo de execução de apenas O(n log n).

# Vamos escrever uma função para encontrar o menor elemento em um array

def busca_menor(arr):
  menor = arr[0] # primeira posição do array
  menor_indice = 0

  for i in range(1, len(arr)):
    if arr[i] < menor:
      menor = arr[i]
      menor_indice = i
  return menor_indice

def ordenacao_por_selecao(arr):
  novo_arr = []
  
  for i in range(len(arr)):
    menor = busca_menor(arr)
    novo_arr.append(arr.pop(menor)) # Sempre vai deletar o menor e adicionar no novo array, sendo assim inserindo do menor para o maior
  return novo_arr

print(ordenacao_por_selecao([5, 3, 6, 2, 10]))