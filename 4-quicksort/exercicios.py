# 4.1 Escreva o código para a função soma, vista anteriormente.
lista = [2, 4, 6]
def soma(lista):
  if len(lista) == 0: # CASO-BASE
    return 0
  else:
    return lista[0] + soma(lista[1:]) # CASO RECURSIVO
print(soma(lista))
# 4.2 Escreva uma função recursiva que conte o número de itens em uma lista

# 4.3 Encontre o valor mais alto em uma lista.

# 4.4 Você se lembra da pesquisa binária do capitulo 1? Ela também é um algoritmo do tipo dividir para conquistar. Você consegue determinar o caso-base e o caso recursivo para a pesquisa binária?