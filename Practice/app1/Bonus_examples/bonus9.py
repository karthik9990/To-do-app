password = input("Enter Password:")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False
digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digits"] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True
result["uppercase"] = upper

print(result)

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")