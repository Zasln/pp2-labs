h=int(input("Ведите число голов: "))
l=int(input("Ведите число ног: "))
def solve(numheads, numlegs):
    chicknum=((numheads*4)-numlegs)/2
    rabbitnum=numheads-chicknum
    print("Количество куриц:",int(chicknum),"Количество кроликов:",int(rabbitnum))
solve(h,l)