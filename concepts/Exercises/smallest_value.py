numbers = [9,41,12,3,74,15]
smallest_so_far = None
print('Before')
for the_num in numbers:
    if smallest_so_far is None:
        smallest_so_far = the_num
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print('After', smallest_so_far)
