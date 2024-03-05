import os
path='C:\Program Files (x86)\Microsoft\Edge\Application'
l=os.listdir(path)
print("Only files:")
for x in l:
    if os.path.isfile(os.path.join(path, x)):
        print(x)
print("Only folders:")
for x in l:
    if os.path.isdir(os.path.join(path, x)):
        print(x)
print("All:")
for x in l:
    print(x)