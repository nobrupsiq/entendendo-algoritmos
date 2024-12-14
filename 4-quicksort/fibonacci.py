def fibonacci(position):
  if position == 1:
    return 0
  if position == 2:
    return 1
  else:
    return fibonacci(position - 1) + fibonacci(position - 2)
  
print(fibonacci(6))

# FUNCAO ITERATIVA

def fibonnaci_iterativa(numero):
  if numero <= 0:
    return 0
  if numero == 1:
    return 1
  
  n1, n2 = 0, 1

  for i in range(2, numero + 1):
    n1, n2 = n2, n1 + n2
  return n2
print(fibonnaci_iterativa(7))