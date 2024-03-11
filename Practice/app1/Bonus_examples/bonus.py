waiting_list = ["sen","ben", "john", "karthik"]
waiting_list.sort()

for index, list in enumerate(waiting_list):
    row = f"{index + 1}.{list.capitalize()}."
    print(row)
