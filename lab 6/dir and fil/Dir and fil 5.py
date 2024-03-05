list = ['a', 'b', 'c', 'd', 'e']
f=open("test.txt", 'a')
for x in list:
    f.write("\n"+x)
f=open("test.txt", 'r')
print(f.read())