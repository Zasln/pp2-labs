import datetime
x=datetime.date.today()
a=x-datetime.timedelta(days=1)
b=x+datetime.timedelta(days=1)
print(a)
print(x)
print(b)