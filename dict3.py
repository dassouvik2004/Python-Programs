def checking_duplicate(dict,student_roll,student_name):
    if student_roll in dict:
        print("Duplicate is not possible")
    else:
        dict[student_roll] = student_name

def data_entry(): 
    my_dict = {}
    while True:
        name = input("Enter the name (or type 'stop'): ")
        if name.lower() == 'stop':
            break
        roll = int(input("Enter the roll: "))
        checking_duplicate(my_dict,roll,name)
    return my_dict

def checkingKey(dict):
    while True:
        roll = input("Enter the roll to check (or type 'stop'): ")
        if roll.lower() == 'stop':
            break
        else:
            roll = int(roll)
            if roll in dict:
                print(f"{roll} exists in the dictionary.")
            else:
                print(f"{roll} does not exist in thr dictionary.")

my_dict = data_entry()
print(my_dict)
checkingKey(my_dict)
