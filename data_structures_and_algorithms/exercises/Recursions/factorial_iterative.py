def factorial(n):
  result=1
  for i in range(1,n+1):
    result *= i
  return result

# test cases
print(factorial(3) == 6)
print(factorial(0) == 1)
print(factorial(5) == 120)
