import one

print("TOP Level in two.py")

one.func()

if __name__=="__main__":
    print("two.py is being run directly")
else:
    print('two.PY has been imported!')
