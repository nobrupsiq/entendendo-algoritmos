# 4.1 Escreva o código para a função soma, vista anteriormente.
lista = [2, 4, 6]
def soma(lista):
  if len(lista) == 0: # CASO-BASE
    return 0
  else:
    return lista[0] + soma(lista[1:]) # CASO RECURSIVO
print(soma(lista))

# 4.2 Escreva uma função recursiva que conte o número de itens em uma lista
lista2 = [6, 5, 3, 9]

def total_items(lista):
  if len(lista) == 0:
    return 0
  else:
    return 1 + total_items(lista[1:]) # O 1 serve como contagem de elemento e não irá somar a tipo 1 + 6(primeiro numero do array)
  
print(total_items(lista2))

# 4.3 Encontre o valor mais alto em uma lista.
lista3 = [5, 23, 12, 54, 34, 19, 77, 34, 22, 67]

def valor_mais_alto(lista):
  if len(lista) == 1: 
    return lista[0]
  else:
    maior_do_resto = valor_mais_alto(lista[1:])
    return lista[0] if lista[0] > maior_do_resto else maior_do_resto # Está dizendo assim, retorne o valor 5 se o valor 5 for maior que o numero 23, se nao retorne o 23 mesmo
      
print(valor_mais_alto(lista3))

# 4.4 Você se lembra da pesquisa binária do capitulo 1? Ela também é um algoritmo do tipo dividir para conquistar. Você consegue determinar o caso-base e o caso recursivo para a pesquisa binária?
def busca_binaria_recursiva(lista, elemento, inicio, fim):
  # Caso base
  if inicio > fim:
    return -1 # Quer dizer que o elemento não foi encontrado

  meio = (inicio + fim) // 2 # Seta o meio da lista

  if lista[meio] == elemento: # Se o meio da minha lista for o alvo que estou procurando
    return meio # irá retornar o numero do meio
  
  elif elemento < lista[meio]:
    # Caso recursivo, se o elemento for menor que o meio da lista, elimina o restante da direita e busca na medate da esquerda
    return busca_binaria_recursiva(lista, elemento, inicio, meio -1)  
  
  else:
    #Caso recursivo, se o elemento nao for menor e sim maior, vai buscar da metade para a direita
    return busca_binaria_recursiva(lista, elemento, inicio, meio +1)