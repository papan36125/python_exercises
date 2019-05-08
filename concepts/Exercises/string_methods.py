print("PrOgRaMiZ".lower())
print("PrOgRaMiZ".upper())
print("This will split all words into a list".split())
print(' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string']))
print('Happy New Year'.find('ew'))
print('Happy New Year'.replace('Happy','Brilliant'))

string = "python is AWesome."

capitalized_string = string.capitalize()

print('Old String: ', string)
print('Capitalized String:', capitalized_string)

string = "Python is awesome"

new_string = string.center(24)

print("Centered String: ", new_string)

string = "Python is awesome"

new_string = string.center(24, '*')

print("Centered String: ", new_string)

string = "PYTHON IS AWESOME"

# print lowercase string
print("Lowercase string:", string.casefold())

firstString = "der Fluß"
secondString = "der Fluss"

# ß is equivalent to ss
if firstString.casefold() == secondString.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal.')
