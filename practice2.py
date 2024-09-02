#Write a python program using for loop to calculate the average of first n natural number
n = int(input("Enter the number of elements: "))
count = 0
for i in range(1,n+1,1):
    count = count+i
av = count/n
print("Average of numbers are: {:.0f}".format(av))