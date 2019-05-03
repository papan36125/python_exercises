# empty list
print(list())

# vowel string
vowelString = 'aeiou'
print(list(vowelString))

# vowel tuple
vowelTuple = ('a', 'e', 'i', 'o', 'u')
print(list(vowelTuple))

# vowel list
vowelList = ['a', 'e', 'i', 'o', 'u']
print(list(vowelList))

# vowel set
vowelSet = {'a', 'e', 'i', 'o', 'u'}
print(list(vowelSet))

# vowel dictionary
vowelDictionary = {'a': 1, 'e': 2, 'i': 3, 'o':4, 'u':5}
print(list(vowelDictionary))

class PowTwo:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        result = 2 ** self.num
        self.num += 1
        return result

powTwo = PowTwo(5)
powTwoIter = iter(powTwo)

print(list(powTwoIter))
