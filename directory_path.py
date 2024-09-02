import os

directory_path = 'c:/Users/ASUS/Education/Dev C++ program'

contents = os.listdir(directory_path)

for i in contents:
    print(i)