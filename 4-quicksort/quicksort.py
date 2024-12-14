#Não há necessidade de ordenar um array vazio ou um array que possua apenas um elemento, certo? então esse será o nosso caso base

'''
1. Escolha um pivô
2. Particione o array em dois subarrays, separando-os entre elementos menores do que o pivô e elemntos maiores do que o pivô
3. Execute o quicksorte recursivamente em ambos os subarrays.
'''

def quicksort(array):
  if len(array) < 2:
    return array

  pivo = array[0]

  menores = [i for i in array[1:] if i <= pivo] # Jeito elegante de fazer um looping
  maiores = [i for i in array[1:] if i > pivo]
  
  return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([3, 5, 2, 1, 4]))

"""
EXPLICAÇÃO PASSO A PASSO NA CHAMADA RECURSIVA

Passo 1:
    Lista inicial: [3, 5, 2, 1, 4]
    Pivô: 3
    Menores: [2, 1] (elementos ≤ 3)
    Maiores: [5, 4] (elementos > 3)
    Retorna: quicksort([2, 1]) + [3] + quicksort([5, 4])
Passo 2 (sublista [2, 1]):
    Lista: [2, 1]
    Pivô: 2
    Menores: [1] (elementos ≤ 2)
    Maiores: [] (elementos > 2)
    Retorna: quicksort([1]) + [2] + quicksort([])
Passo 3 (sublista [1]):
    Lista: [1]
    É uma lista com apenas um elemento, então retornamos [1].
Passo 4 (sublista [5, 4]):
    Lista: [5, 4]
    Pivô: 5
    Menores: [4] (elementos ≤ 5)
    Maiores: [] (elementos > 5)
    Retorna: quicksort([4]) + [5] + quicksort([])
Passo 5 (sublista [4]):
    Lista: [4]
    É uma lista com apenas um elemento, então retornamos [4].
Combinação dos resultados:
    Sublista [2, 1] → quicksort([1]) + [2] + quicksort([]) = [1, 2]
    Sublista [5, 4] → quicksort([4]) + [5] + quicksort([]) = [4, 5]
    Lista completa → [1, 2] + [3] + [4, 5] = [1, 2, 3, 4, 5]
"""