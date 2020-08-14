num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")


Output:

venv) root@kali:~/PycharmProjects/hello# python Demo1.py
Enter a number: 11
11 is a prime number
(venv) root@kali:~/PycharmProjects/hello# python Demo1.py
Enter a number: 15
15 is not a prime number
3 times 5 is 15

