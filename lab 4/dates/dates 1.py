import datetime
x=datetime.datetime.now()
print(int(x.day)-5, x.strftime("%B"), x.year)