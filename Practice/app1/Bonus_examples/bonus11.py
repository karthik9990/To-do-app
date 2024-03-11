def get_average():
    with open("files/data.txt", 'r') as file:
        data = file.readlines()
        values = data[1:]
        values = [float(i) for i in values]

        average_local = sum(values) / len(values)
    return average_local


average = get_average()
print(average)


def get_average():
    x = "hello"
    return x.capitalize()


print(get_average())


def get_average():
    x = "hello"
    return x.capitalize()


get_average()


def get_average():
    print("Hi")
    x = "hello"
    return x.capitalize()


get_average()


def get_average():
    print("Hi")
    x = "hello"


print(get_average())
