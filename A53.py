def fun(no):
    if no>=1:

        no = no -1;
        fun(no)
        print(no, end=" ")

def main():
    val = int(input("Enter no"))
    fun(val)
    print(" ")


if __name__ == "__main__":
    main()
