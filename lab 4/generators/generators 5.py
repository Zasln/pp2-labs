n=int(input())
def gen(n):
    x=n
    while x>=0:
        yield x
        x=x-1
num=gen(n)
for x in num:
    print(x)