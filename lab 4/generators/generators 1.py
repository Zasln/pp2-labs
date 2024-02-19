n=int(input())
def gen(n):
    x=0
    for i in range(n+1):
        yield x*x
        x=x+1
num=gen(n)
for x in num:
    print(x)