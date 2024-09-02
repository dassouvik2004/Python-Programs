def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)
fact = 0
num = int(input("Enter the number: "))
fact = factorial(num)
print(f"Factorial of {num} is",fact)