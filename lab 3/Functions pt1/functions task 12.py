str = input()
def if_palindrome(str):
    str2 = str[::-1]
    if str==str2:
        print("Palindrome")
    else:
        print("Not palindrome")
if_palindrome(str)