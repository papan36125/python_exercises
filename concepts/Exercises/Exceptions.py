# import module sys to get the type of exception
import sys
import traceback
randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except ValueError:
        print('Oops! ValueError has occured!')
        print(sys.exc_info()[1])
        error_traceback= sys.exc_info()[2]
        tb=''.join(traceback.format_tb(error_traceback))
        print(tb)
        print("Next entry.")
        print()
    except (TypeError, ZeroDivisionError):
       # handle multiple exceptions
       # TypeError and ZeroDivisionError
       print('Oops!', sys.exc_info()[0], 'has occured!')
       print(sys.exc_info()[1])
       error_traceback= sys.exc_info()[2]
       tb=''.join(traceback.format_tb(error_traceback))
       print(tb)
       print("Next entry.")
       print()
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print(sys.exc_info()[1])
        error_traceback= sys.exc_info()[2]
        tb=''.join(traceback.format_tb(error_traceback))
        print(tb)
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)

print('\n****************************************************\n')
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)

print('\n****************************************************\n')
try:
   f = open("test.txt",encoding = 'utf-8')
   print(f.read())
finally:
   f.close()
