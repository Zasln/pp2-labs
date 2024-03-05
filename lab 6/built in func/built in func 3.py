str=input()
cnt=0
for i in range(0, len(str)):
    if str[i]==str[len(str)-1-i]:
        cnt=cnt+1
    elif str[i]!=str[len(str)-1-i]:
        print("Not a palindrome")
        break
if cnt==len(str):
    print("Palindrome")