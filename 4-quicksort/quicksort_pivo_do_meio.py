def quicksort(list):
  if len(list) < 2:
    return list
  
  left = 0
  right = len(list) -1
  meio = (left + right) // 2
  pivo = list[meio]

  menores = [i for i in list if i < pivo]
  iguais = [i for i in list if i == pivo]
  maiores = [i for i in list if i > pivo]

  return quicksort(menores) + iguais + quicksort(maiores)

print(quicksort([7,3,6,9,10,1,5]))