total = 0
count = 0
print('Before', count, total)
for val in [9,41,12,3,74,15]:
    total += val
    count += 1
    print( count, total, val)
print('After', count, total, total/count)
