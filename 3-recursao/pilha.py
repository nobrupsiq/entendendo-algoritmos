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


# RECAPITULANDO
'''
Recursão é quando uma função chama a si mesma.
Toda função recursiva tem dois casos: o caso-base e o caso recursivo.
Uma pilha tem duas operações: push e pop
Todas as chamadas de função vão para a pilha de chamada. (CallStack)
A pilha de chamada pode ficar muito grande e ocupar muita memória.
'''