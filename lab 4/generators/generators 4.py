a = int(input())
b = int(input())
def squares(a, b):
    x=a
    for x in range(a, b):
        yield x*x
num=squares(a, b)
for x in num:
    print(x)