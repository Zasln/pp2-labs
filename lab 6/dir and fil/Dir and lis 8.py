import os
path=r"C:\Users\Public\Music\svbsb.txt"
f=os.access(path, os.F_OK)
if f:
    os.remove(path)
    print("Removed: "+path)
else:
    print("File doesn't exists")