mylist = [10,20,30,40]
print("Before reversing: ",mylist)
new_list = mylist[::-1]
print("Using slicing: ",new_list)
new_list.reverse()
print("Using reverse: ",mylist)
print("Using reversed: ",list(reversed(mylist)))