for i in range(100,900+1,1):
    n = i
    x = n
    sum = 0
    while(n>0):
        rem = n%10
        count = rem**3
        sum = sum+count
        n = n//10
        if x == sum:
            print(x,"is an armstrong number.")
        else:
            pass