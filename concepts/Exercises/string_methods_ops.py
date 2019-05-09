word = 'fanana'
if word == 'banana':
    print('All right, bananas')
if word < 'banana':
    print("Your word, " + word +', comes before banana.')
elif word > 'banana':
    print("Your word, " + word +', comes after banana.')
else:
    print('All right, bananas.')

greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
nnn = greet.upper()
print(nnn)
print(greet)
print('Hi There'.lower())

fruit = 'banana'
pos = fruit.find('na')
print(pos)
aa = fruit.find('z')
print(aa)

nstr = greet.replace('Bob', 'Jane')
print(nstr)
print(greet)
nstr = greet.replace('o','X')
print(nstr)
print(greet)

greet = '   Hello Bob    '
greet_2 = greet.lstrip()
print(greet_2)
greet_2 = greet.rstrip()
print(greet_2)
greet = '   Hello Bob    '
greet_2 = greet.strip()
print(greet_2)



line = 'Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('p'))
