from array import *

array1 = array('i', [10,20,30,40,50])

for x in array1:
 print(x)

print (array1[0])

print (array1[2])

array1.insert(1,60)
print("After insertion")
for x in array1:
 print(x)

array1.remove(20)
print("After deletion")
for x in array1:
 print(x)

print ('The value of 40 is at index::',array1.index(40))

array1[2] = 80
print('After Update')
for x in array1:
 print(x)
