try:
    width = float(input("Enter Rectangle width: "))
    length = float(input("Enter Rectangle length: "))

    if width == length:
        exit("that looks like a square.")

    area = width * length
    print(area)
except ValueError:
    print("Please enter a number ")

# example

try:
    value = float(input("Enter value: "))
    total = float(input("Enter total value: "))

    calculate = value/total * 100

    print(f"that is {calculate}%")
except ValueError:
    print("Please Enter a number for the value and total")
    exit()

