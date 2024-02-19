n=int(input())
def gen(n):
    x=0
    for x in range(n):
        if x%4==0 and x%3==0:
            yield x
            x=x+1
num=gen(n)
for x in num:
    print(x, end=", ")