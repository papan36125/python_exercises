def greet(*names):
   """This function greets all
   the person in the names tuple."""

   # names is a tuple with arguments
   print(type(names))
   for name in names:
       print("Hello",name)

greet("Monica","Luke","Steve","John")
