def fun(no):
    if no>0:
        print("*" , end=" ")
        no = no -1;
        fun(no)


def main():
    val = int(input("Enter no"))
    fun(val)
    print(" ")


if __name__ == "__main__":
    main()
