l=[1, 2, 8]
if len(l)<1:
    print("No elements in a list")
elif len(l)==1:
    print(l[0])
else:
    a=eval(str(l[0]*l[1]))
    for i in range(2, len(l)):
        a=eval(str(a*l[i]))
    print(a)