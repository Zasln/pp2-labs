str=input()
def reverse(str):
    list=str.split()
    list.reverse()
    for x in list:
        print(x, end =' ')
reverse(str)