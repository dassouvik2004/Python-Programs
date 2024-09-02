def full_peramids(n):
    alph = 65
    for i in range(1,n+1):
        for j in range(n - i):
            print(" ",end = " ")
        for k in range(1,2*i):
            print(chr(alph),end=" ")
            alph += 1
        alph = 65
        print()
full_peramids(10)

def num_pyramids(n):
    for i in range(1,n+1):
        for k in range(n - i):
            print(" ",end=" ")
        for j in range(1,2*i):
            print("*",end=" ")
        print()
num_pyramids(5)

def diamond_pyramids(n):
    for i in range(1,n+1):
        for k in range(n - i):
            print(" ",end=" ")
        for j in range(1,2*i):
            print("*",end=" ")
        print()
    for i in range(n-1,0,-1):
        for k in range(n - i):
            print(" ",end=" ")
        for j in range(2*i-1):
            print("*",end=" ")
        print()
diamond_pyramids(5)
def half_inverted_pyramid(n):
    alph = 65
    for i in range(1,n):
        for j in range(1,2*i):
            print(chr(alph),end=" ")
            alph += 1
        alph = 65
        print()
half_inverted_pyramid(5)