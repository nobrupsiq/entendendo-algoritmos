caderno = dict()

caderno['maca'] = 0.67
caderno['leite'] = 1.49
caderno['abacate'] = 1.49

print(caderno['maca'])

'''
EXERCICIOS
Quais destas funções hash são consistentes?

5.1 f(x) = 1
Resposta: Consistente
5.2 f(x) = rand()
Resposta: Inconsistente
5.3 f(x) = proximo_espaco_vazio()
Resposta: Inconsistente
5.4 f(x) = len(x)
Resposta: Consistente
'''

# As tabelas hash são ótimas opções quando:
# Você deseja mapear algum item com relação a outro
# Você precisa pesquisar algo

lista_telefonica = {}
lista_telefonica['jenny'] = 8675309
lista_telefonica['emergency'] = 911 

print(lista_telefonica['jenny'])