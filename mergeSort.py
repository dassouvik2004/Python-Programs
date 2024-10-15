def merge(arr,beg,mid,end):
    temp = []
    i = beg
    j = mid + 1
    while i<=mid and j<=end:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i<=mid:
        temp.append(arr[i])
        i += 1
    while j<=end:
        temp.append(arr[j])
    k = 0
    for i in range(beg,end+1):
        arr[i] = temp[k] 
        k += 1

def mergeSort(arr,beg,end):
    if beg<end:
        mid = (end+beg)//2
        mergeSort(arr,beg,mid)
        mergeSort(arr,mid+1,end)
        merge(arr,beg,mid,end)
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    arr.append(int(input("Enter number {}: ".format(i+1))))
print("Before sorting: ")
print(arr)
mergeSort(arr,0,n-1)
print("After sorting:  ")
print(arr)