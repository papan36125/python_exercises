list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print( "list1[0]: ", list1[0])
print( "list2[1:5]: ", list2[1:5])
print( "Value available at index 2 : ", list1[2])
list1[2] = 2001
print ("New value available at index 2 : ",list1[2])
print ("Before deleting value at index 2 : ")
print (list1)
del list1[2]
print ("After deleting value at index 2 : ")
print (list1)
print("\n******************************************\nBasic List Operations\n")
print('Length of [1, 2, 3]:',len([1, 2, 3]))
print('Concatenation [1, 2, 3] + [4, 5, 6]:',[1, 2, 3] + [4, 5, 6])
print('Repetition [\'Hi!\'] * 4:',['Hi!'] * 4)
print('Membership 3 in [1, 2, 3]:',3 in [1, 2, 3])
print('Iteration')
for x in [1, 2, 3]: print (x)
