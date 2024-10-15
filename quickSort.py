def partition(arr,left,right):
    loc = left
    while True:
        while arr[loc]<=arr[right] and loc!=right:
            right += -1
        if loc == right:
            break
        else:
            arr[loc],arr[right]  = arr[right],arr[loc]
            loc = right
        while arr[loc]>=arr[left] and loc!=left:
            left += 1
        if loc == left:
            break
        else:
            arr[loc],arr[left] = arr[left], arr[loc]
            loc = left
    return loc
def quickSort(arr,left,right):
    if left<right:
        loc = partition(arr,left,right)
        quickSort(arr,left,loc-1)
        quickSort(arr,loc+1,right)
arr = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    arr.append(int(input("Enter number {}: ".format(i+1))))
print("Before sorting: ")
print(arr)
quickSort(arr,0,n-1)
print("After sorting: ")
print(arr)