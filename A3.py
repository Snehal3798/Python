'''3. Write a program which contains one class named as Arithmetic.
Arithmetic class contains three instance variables as Value1 ,Value2.
Inside init method initialise all instance variables to 0.
There are three instance methods inside class as Accept(), Addition(), Subtraction(),
Multiplication(), Division().
Accept method will accept value of Value1 and Value2 from user.
Addition() method will perform addition of Value1 ,Value2 and return result.
Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
Division() method will perform division of Value1 ,Value2 and return result.
After designing the above class call all instance methods by creating multiple objects.
'''


class Arithmetic:
    def __int__(self):
        self.val1 = 0
        self.val2 = 0

    def Accept(self):
        print("Enter First no")
        self.val1 = int(input())

        print("Enter second no")
        self.val2 = int(input())

    def Add(self):
        return self.val1+self.val2;

    def sub(self):
        return self.val1-self.val2;
    def mul(self):
        return self.val1*self.val2;
    def dive(self):
        return self.val1/self.val2;

def main():
    obj1 =Arithmetic()
    obj2=Arithmetic()
    obj1.Accept()
    print("Addition{0}\nSubstration{1}\nMultiplication{2}\nDivision{3}".format(obj1.Add(),obj1.sub(),obj1.mul(),obj1.dive()))

    obj2.Accept()
    print("Addition{0}\nSubstration{1}\nMultiplication{2}\nDivision{3}".format(obj2.Add(), obj2.sub(), obj2.mul(),obj12.dive()))
    print(end="")
if __name__=="__main__":
    main()