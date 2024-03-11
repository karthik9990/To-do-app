member = input("Enter New Member Name: ")
file = open("members.txt", 'r')
existing_members = file.readlines()
file.close()
existing_members.append(member + "\n")

file = open("members.txt", 'w')
existing_members = file.writelines(existing_members)
file.close()