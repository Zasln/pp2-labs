from datetime import date, datetime
y=int(input())
m=int(input())
d=int(input())
da=date(y, m, d)
print("First date:",da)
y1=int(input())
m1=int(input())
d1=int(input())
da1=date(y1, m1, d1)
print("Second date:",da1)
dif=abs((y-y1))*365*24*60*60+abs(m-m1)*30*24*60*60+abs(d-d1)*24*60*60
print("Diffrence in seconds is approximately:",dif)