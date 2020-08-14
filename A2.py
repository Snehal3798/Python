'''2. Write a program which contains one class named as Circle.
Circle class contains three instance variables as Radius ,Area, Circumference.
That class contains one class variable as PI which is initialise to 3.14.
Inside init method initialise all instance variables to 0.0.
There are three instance methods inside class as Accept(), CalculateArea(),
CalculateCircumference(), Display().
Accept method will accept value of Radius from user.
CalculateArea() method will calculate area of circle and store it into instance variable Area.
CalculateCircumference() method will calculate circumference of circle and store it into instance
variable Circumference.
And Display() method will display value of all the instance variables as Radius , Area,
Circumference.
After designing the above class call all instance methods by creating multiple objects.'''


class Circle:
    PI = 3.14;

    def __init__(self):
        self.radius = 0.0;
        self.area = 0.0
        self.cer = 0.0

    def Accept(self):
        print("Enter the value")
        self.radius = float(input())

    def Area(self):
        self.area = self.PI * self.radius ** 2;

    def Circumference(self):
        self.cer = self.PI * self.radius * 2;

    def Display(self):
        print("area is{0}\n circumference is{1}".format(self.area, self.cer))


def main():
    obj1 = Circle()
    obj2 = Circle()
    obj3 = Circle()
    obj4 = Circle()

    obj1.Accept()
    obj1.Area()
    obj1.Circumference()
    obj1.Display()

    obj2.Accept()
    obj2.Area()
    obj2.Circumference()
    obj2.Display()

    obj3.Accept()
    obj3.Area()
    obj3.Circumference()
    obj3.Display()

    obj4.Accept()
    obj4.Area()
    obj4.Circumference()
    obj4.Display()

if __name__ == "__main__":
    main()
