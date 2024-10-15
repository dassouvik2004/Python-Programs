my_list = [10,50,30,5,20]
print("Original List:",my_list)
my_list.sort()
print("Sorting using sorted method(Ascending Order):",my_list)
my_list.sort(reverse=True)
print("Sorting using sort method(Descending Order):",my_list)
new_list = [20,40,10,50,30]
print("Original List:",new_list)
sorted_list1 = sorted(new_list)
print("Sorting using sorted function(Ascending Order):",sorted_list1)
sorted_list2 = sorted(new_list,reverse=True)
print("Sorting using sorted function(Descending Order):",sorted_list2)