def fun():
    num = int(input("Enter number"))

    for i in range(1, num):
        for j in range(num, i, -1):
            print("*", end='')

        print("")


fun()