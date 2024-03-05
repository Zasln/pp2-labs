f=open("A.txt", 'a')
f1=open("test.txt")
for x in f1:
    f.write(x)
f.close
f1.close