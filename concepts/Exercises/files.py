with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("This is my first file\n")
   f.write("This file\n")
   f.write("contains three lines\n")

f = open("test.txt",'r',encoding = 'utf-8')
print(f.read(4))
print(f.read(4))
print(f.read())
print(f.read())
print(f.tell())
f.seek(0)
print(f.read())
f.seek(0)
for line in f:
    print(line, end = '')
f.seek(0)
print(f.readline())
print(f.readline())
print(f.readline())
f.seek(0)
print(f.readlines())
f.close()
