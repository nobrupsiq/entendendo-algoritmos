# RECURSÃO

# def regressiva(i):
#   print(i)
#   regressiva(i -1)

# regressiva(3)

# Quando você escreve uma função recursiva, deve informar quando a recursão deve parar. É por isso que toda função recursiva tem duas partes: O caso-base e o caso recursivo. O caso recursivo é quando a função chama a si mesma. O caso-base é quando a função não chama a si mesma novamente, de forma que o programa não se torna um loop infinito.

# VAMOS ADICIONAR O CASO BASE A FUNÇÃO RECURSIVA

def regressiva(i):
  print(i)
  if i <= 1: # CASO BASE
    return
  else: # CASO RECURSIVO
    regressiva(i - 1)

regressiva(3)