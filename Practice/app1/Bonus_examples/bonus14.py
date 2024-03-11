from Practice.app1.Bonus_examples.convertors import convert
from Practice.app1.Bonus_examples.parsers14 import parse

feet_inches = input("Enter feet and inches:")

parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Kid is too small and can't slide")
else:
    print("Kid can use the slide.")
