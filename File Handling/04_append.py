with open("File_05.txt",'a+') as f:
    content = f.write("Hello,Souvik!\n")
    f.seek(0)
    for line in f:
        print(f.readline(),end = " ")