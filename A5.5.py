def fun(num):
    if num == 1:
        return num

    else:
        return num * fun(num - 1)


def main():
    val = int(input("ENter the no"))
    fun(val)
    print("factorial of no", fun(val))


if __name__ == "__main__":
    main()

