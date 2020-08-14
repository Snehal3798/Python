from typing import List


def add():
    arr = list()
    num = int(input("Enter the number of elements"))
    for i in range(num):
        numbers = int(input("enter number"));
        arr.append(numbers)
    print("Sum of elements", sum(arr))


add()

Output:
Enter the number of elements 4
enter number4
enter number2
enter number7
enter number8
Sum of elements 21