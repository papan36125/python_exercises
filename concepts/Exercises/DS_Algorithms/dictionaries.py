dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print( "dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

del dict['Name']; # remove entry with key 'Name'
print(dict)
dict.clear();     # remove all entries in dict
print(dict)
del dict ;        # delete entire dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print ("dict['Name']: ", dict['Name'])
