def check_each(*args):
    for i in args:
        if i >5:
            print(f"numero {i}: bigger")
        elif i<5:
            print(f"numero {i}: smaller")
        else:
            print(f" numero {i}: equal")


check_each(12,3,4,5,6)



