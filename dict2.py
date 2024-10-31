def checkingKey(dict,key):
    if key in dict:
        print(f"{key} exist...")
    else:
        print(f"{key} does not exists.")

my_dict = {'name':'Souvik','roll':119,'stream':'BCA'}
key1 = 'class'
checkingKey(my_dict,key1)