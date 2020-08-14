def fun(no1):
    s1 = ''
    for i in no1:
        s1 = i + s1
    return s1


input_str = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

print('Reverse String  =', fun(input_str))



output: root@kali:~/PycharmProjects/hello# python Hello.py
Reverse String  = 10987654321
