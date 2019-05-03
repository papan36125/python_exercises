# Operating System List
os = ['Windows', 'macOS', 'Linux']
print('Original List:', os)

# List Reverse
os.reverse()

# updated list
print('Updated List:', os)
# Operating System List
os = ['Windows', 'macOS', 'Linux']
print('Original List:', os)

# Reversing a list
#Syntax: reversed_list = os[start:stop:step]
reversed_list = os[::-1]

# updated list
print('Updated List:', reversed_list)

# Operating System List
os = ['Windows', 'macOS', 'Linux']

# Printing Elements in Reversed Order
for o in reversed(os):
    print(o)
