def factorial(n):
  if n < 0:
    ValueError("Inputs 0 or greater only")
  if n <= 1:
    return 1
  return n * factorial(n - 1)

factorial(3)
# 6
factorial(4)
# 24
factorial(0)
# 1
factorial(-1)
