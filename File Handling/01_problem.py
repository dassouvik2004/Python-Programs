with open("file2.txt") as f:
    content = f.read()
    if "twinkle" in content:
        print("The twinkle is present in the content")
    else:
        print("The twinkle is not present in the content")