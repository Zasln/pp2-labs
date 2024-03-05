import os
path=r"C:\Windows\diagnostics\scheduled\Maintenance\ru-RU"
if os.path.exists(path):
    print("path exists")
    print("file name:")
    print(os.path.basename(path))
    print("Directory portion:")
    print(os.path.dirname(path))
else:
    print("path don't exists")
