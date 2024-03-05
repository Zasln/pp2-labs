str1=input()
cnt=0
for x in str1:
    if ord(x)>=65 and ord(x)<=90:
        cnt=cnt+1
print("Number of Upper char is: "+str(cnt))
cnt=0
for x in str1:
    if ord(x)>=97 and ord(x)<=122:
        cnt=cnt+1
print("Number of Lower char is: "+str(cnt))
