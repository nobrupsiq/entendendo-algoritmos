'''
    Solicita uma URL do facebook
       Está URL está na hash?
   
     SIM:               NAO:
  retorna os       Faz o servidor
dados do cache  Executar alguma tarefa
'''

#FORMA DE CÓDIGO

cache = {}
def pega_dados_do_servidor():
  print('PEGANDO URL DO SERVIDOR')

def pega_pagina(url):
  if cache.get(url):
    return cache[url] # 1
  else:
    dados = pega_dados_do_servidor(url)
    cache[url] = dados # 2
    return dados
  
# 1 - retorna dados do cache
# 2 - retorna dados do servidor

# RECAPITULANDO

'''
As tabelas hash são úteis para
* Modelar relações entre dois itens
* Filtrar por duplicatas
* Caching/memorização de dados, em vez de solicitar estes dados do servidor.
'''

'''
Desempenho da tabela hash
        CASO MEDIO   PIOR CASO
PROCURA    O(1)         O(N)
INSERÇÃO   O(1)         O(N)
REMOÇÃO    O(1)         O(N)
'''