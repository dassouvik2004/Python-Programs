def check_duplicate(collect_data,data_name,data_id):
    if data_id in collect_data:
        print("Duplicate is not possible")
    else:
        collect_data[data_id] = data_name
def dataEntry():
    collect_data = {}
    while True:
        data_name = input("Enter your name (or type 'stop'): ")
        if data_name.lower() == 'stop':
            break
        data_id = int(input("Enter your id: "))
        check_duplicate(collect_data,data_name,data_id)
    return collect_data
data = dataEntry()
print(f'The data is {data}')