"""
[baixo, ...., alto]
baixo = primeiro item do array 
alto = ultimo item do array

A cada tentativa, você testa para o elemento central
Exemplo: meio = (baixo + alto) / 2 # Desta maneira eu sempre irei ter o valor central
Chute = lista[meio] # O chute sempre vai começar no meio da lista
OBS: a variavel 'meio' será arredondado para baixo automaticamente pelo Python se (baixo + alto) não for um número par
"""

def pesquisa_binaria(lista, item):
  baixo = 0 # 1° Baixo e alto acompanham a parte da lista que você está procurando.
  alto = len(lista) -1
  while baixo <= alto: # 2° Enquanto ainda não conseguiu chegar a um único elemento...
    meio = (baixo + alto) // 2 # 3° ...Verifica o elemento central.
    chute = lista[meio]
    if chute == item: # 4° Acha o item.
      return meio
    if chute > item: # 5° O chute foi muito alto.
      alto = meio - 1 
    else: # 6° O chute foi muito baixo.
      baixo = meio + 1 
  return None # 7° O item não existe.

minha_lista = [1, 3, 5, 7, 9] # Lembrando, as listas começam no indice 0
print(pesquisa_binaria(minha_lista, 3))