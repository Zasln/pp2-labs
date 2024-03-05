import os
path=r"C:\Windows\assembly\GAC_64\Microsoft.Ink\6.1.0.0__31bf3856ad364e35\Microsoft.Ink.dll"   
f=os.access(path, os.F_OK)
print(f)
f2=os.access(path, os.R_OK)
print(f2)
f3=os.access(path, os.W_OK)
print(f3)
f4=os.access(path, os.X_OK)
print(f4)