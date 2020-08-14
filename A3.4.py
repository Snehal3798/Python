lst = []
num = int(input("Enter the no of elements"))
for i in range(num):
    numbers = int(input("Enter Number"))
    lst.append(numbers)


def freq(lst, x):
    count = 0
    for i in lst:
        if i == x:
            count += 1
        return count


x = int(input("Elements to search"))
print(freq(lst,x))
