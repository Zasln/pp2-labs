q = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    num = int(input())
    q.append(num)
def filter_prime(q):
    prime_list=[]
    for x in q:
        if x>=2 and x%2!=0:
            prime_list.append(x)
    for x in prime_list:
        for i in range (2, int(x/2)+1):
            if x%i==0:
                prime_list.remove(x)
    print(prime_list)
filter_prime(q)