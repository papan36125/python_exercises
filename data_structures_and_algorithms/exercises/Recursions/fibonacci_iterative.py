def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n
  n1=1
  n2=1
  result = 0
  count=2
  while count<n:
    result = n1+n2
    count+=1
    n1=n2
    n2 = result
  return result



# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)
