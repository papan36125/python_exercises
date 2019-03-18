def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(3)
# 2
fibonacci(7)
# 13
fibonacci(0)
# 0
