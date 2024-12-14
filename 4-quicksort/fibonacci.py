def fibonacci(position):
  if position == 1:
    return 0
  if position == 2:
    return 1
  else:
    return fibonacci(position - 1) + fibonacci(position - 2)
  
print(fibonacci(6))