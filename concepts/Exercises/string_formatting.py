# string formatting

# using triple quotes
print('''He said, "What's there?"''')

# escaping single quotes
print('He said, "What\'s there?"')

# escaping double quotes
print("He said, \"What's there?\"")

print("C:\\Python32\\Lib")
print("This is printed\nin two lines")
print("This is \x48\x45\x58 representation")
print("This is \x61 \ngood example")
print(r"This is \x61 \ngood example")

# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)

# formatting integers
print("Binary representation of {0} is {0:b}".format(12))
# formatting floats
print("Exponent representation: {0:e}".format(1566.345))
# round off
print("One third is: {0:.3f}".format(1/3))
# string alignment
print("|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham'))

# old method
x = 12.3456789
print('The value of x is %3.2f' %x)
print('The value of x is %3.4f' %x)
