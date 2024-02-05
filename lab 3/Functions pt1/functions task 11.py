str=input()
list=str.split()
list=[int(i) for i in list]
def unique(list):
    unique_list = []
    for x in list:
        if x not in unique_list:
            unique_list.append(x)
    print(unique_list)
unique(list)