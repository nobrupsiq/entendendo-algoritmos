# Suponha que você tenha esta simples função que imprime na tela todos os itens de uma lista:
def imprime_itens(lista):
  for item in lista:
    print(item)
# Esta função analisa cada item da lista e o imprime. Como esta função passa por toda a lista uma vez, ela tem tempo de execução O(n). Agora, imagine que você modificou esta função para que ela agurde um segundo antes de imprimir um item:
from time import sleep
def imprime_itens2(lista):
  for item in lista:
    sleep(1)
    print(item)

lista = [2, 4, 6, 8, 10]
print(imprime_itens(lista))          
print(imprime_itens2(lista))

# C * N (Onde C é alguma quantidade determinada de tempo que o seu algoritmo leva para ser executado. Ela é chamada de CONSTANTE. Pode ser, por exemplo 10 milissegundos * N para a função imprime_itens contra 1 segundo * N para a função imprime_itens2

# CASO MÉDIO VERSUS PIOR CASO.

# SE NÓS SEMPRE ECOLHERMOS O PRIMEIRO ELEMENTO PARA SER O NOSSO PIVÔ A NOSSA PILHA DE CHAMADA TERÁ O TOTAL DE PESO 8
# SE ESCOLHERMOS SEMPRE O ELEMENTO DO MEIO PARA SER O NOSSO PIVÔ, A NOSSA PILHA TERÁ PESO 4