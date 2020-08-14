from functools import *;


def fun():
    size = int(input("Enter number of elements"));
    arr = list();
    print("Enter the elements");
    for i in range(0, size, 1):
        print("Enter number", i + 1)
        no = int(input());
        arr.append(no);
    return arr;


def eve(no):
    if ((no % 2) == 0):
        return True
    else:
        return False


def mev(no):
    return no ** 2


def rev(no1,no2):
    return no1+no2;


raw = fun();
print("Accepted data is ");
print(raw);
farr = list(filter(eve, raw))
print("Data after filter", farr)

arr1 = list(map(mev, farr))
print("Data after MAp", arr1)

arr2 = list(reduce(rev, arr1))
print("Data after Reduce", arr2)