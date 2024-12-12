def sauda(nome): # PILHA DE CHAMADA
  print(f'Olá {nome}')
  sauda2(nome)
  print(f'preparando para dizer tchau...')
  tchau()

def sauda2(nome): # TOPO DA PILHA
  print(f'Como vai {nome}?')

def tchau():
  print('Ok, tchau!')

sauda("Bruno")


def fat(x):
  if x == 1:
    return 1
  else:
    return x * fat(x-1)

print(fat(3))
