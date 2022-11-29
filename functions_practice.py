def hello():
    print("Hello, user!")


def pack(a, b, c):
    return [a, b, c]


def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty!")

    else:
        for i in range(len(list)):
            if i == 0:
                print(f"First I eat {list[0]}")
            else:
                print(f"Next I eat {list[i]}")


list = pack("Cheese", "Apple", "Steak")

hello()
print(list)
eat_lunch([])
eat_lunch(list)
