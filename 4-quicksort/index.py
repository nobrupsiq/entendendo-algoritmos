lista = [2, 4, 6]

def soma(lista):
  if len(lista) == 0:
    return 0
  else:
    return lista[0] + soma(lista[1:])

print(soma(lista))

#DICA: Quando estiver escrevendo uma função de recursãopo que envolva um array, o caso-base será, muitas vezes, um array vazio ou um array com apenas um elemento. Se estiver com problemas, use este caso como base. 