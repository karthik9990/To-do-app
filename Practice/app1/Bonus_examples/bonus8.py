date = input("Enter today's Date - Format YYYY-MM-DD: ")
mood = input("How do you rate your mood from 1 to 10?: ")
thoughts = input("Let your thoughts flow: \n")
with open(f"../Journal/{date}.txt", 'w') as file:
    file.write("The mood is: " + mood + 2 * '\n')
    file.write(thoughts)