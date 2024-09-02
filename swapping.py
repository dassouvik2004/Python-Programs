def swap(x,y):
    x,y = y,x
    return x,y
a = 10
b = 20
print("Before swapping:",a,b)
a,b = swap(a,b)
print("After swapping:",a,b)
