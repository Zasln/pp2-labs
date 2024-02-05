str=input()
list=str.split()
list=[int(i) for i in list]
def histogram(list):
    for x in list:
        print('*'*x)
histogram(list)