tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
tup1 = ()
tup1 = (50,)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples because they are immutable
# tup1[0] = 100

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print( tup3)

tup = ('physics', 'chemistry', 1997, 2000)
print (tup)
del tup
# print ("After deleting tup : ")
# print( tup)
print("\n******************************************\nBasic List Operations\n")
print('Length of (1, 2, 3):',len((1, 2, 3)))
print('Concatenation (1, 2, 3) + (4, 5, 6):',(1, 2, 3) + (4, 5, 6))
print('Repetition ()\'Hi!\') * 4:',('Hi!',) * 4)
print('Membership3 in (1, 2, 3):',3 in (1, 2, 3))
print('Iteration')
for x in (1, 2, 3): print (x)
