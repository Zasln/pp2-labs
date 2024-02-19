n=int(input())
def gen(n):
    x=0
    for i in range(n):
        if i%2==0:
            yield x
            x=x+2
num=gen(n)
for x in num:
    print(x, end=", ")