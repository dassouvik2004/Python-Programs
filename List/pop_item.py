#Basically popitem() method is used with dictionaries, not lists in python
dict1 = {'a':1,'b':2,'c':3}
key,value = dict1.popitem()
print(key,value)

#pop() method is used with lists in python
list1 = [10,20,30]
item = list1.pop()
print(item)