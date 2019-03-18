numbers = [10,20,30,40.5,50]
# print(numbers[0])
#data retrieval -> O(1) if index is known
# numbers[1] = 'Adam'
# print(numbers[1])
# for num in numbers:
	# print(num)

# for i in range(len(numbers)):
# 	print(numbers[i])

# print(numbers[:-2])
# O(N) search running time
max = numbers[0]
for num in numbers:
	if num > max:
		max = num
print(max)

