l = [1, 3, 4, 0]
print(any(l))

l = [0, False]
print(any(l))

l = [0, False, 5]
print(any(l))

l = []
print(any(l))
s = "This is good"
print(any(s))

# 0 is False
# '0' is True
s = '000'
print(any(s))

s = ''
print(any(s))

d = {0: 'False'}
print(any(d))

d = {0: 'False', 1: 'True'}
print(any(d))

d = {0: 'False', False: 0}
print(any(d))

d = {}
print(any(d))

# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))
