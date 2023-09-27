class Human(object):
    """Human class"""

    def __init__(self, name, age, height, gender):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender

    @classmethod
    def change_name(cls, new_name):
        test = new_name

    test = "my height"

    def print_hello(self):
        print("Hello")

    @staticmethod
    def print_other():
        print("*play music*")


bob = Human("Bob", 35, 72, "m")
charles = Human("Charles", 22, 70, "m")


class PostalAddress:
    postalCode = 12345  # class Variable

    def __init__(self, name="Default Name", street="Central Street - 1"):
        self.name = name
        self.street = street

    @classmethod
    def new_postal_code(cls, newcode):
        cls.postalCode = newcode


class CellPhone:
    def __init__(self, brand, number):
        self.brand = brand
        self.number = number

    # @property
    # def number(self):


# iphone = CellPhone.iphone("123-456-8899")
# iphone.get_number()
# iphone.get_emergency_number()

#
#
#
# cP0 = PostalAddress()
# print(cP0.postalCode)
#
# PostalAddress.postalCode = 4321
#
#
# print(cP0.postalCode)
#
# cP1 = PostalAddress()
# print(cP1.postalCode)
#


my_id = 123


class Person:
    """Initializing the variables"""

    gf = None
    name = ""
    age = 0
    location = None
    house = "abcd"

    # defining constructor
    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

    # Defining class methods
    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)


# Def of sublcass tarts here
class Student(Person):
    student_id = ""

    def __init__(self, student_name, student_age, student_id):
        super().__init__(student_name, student_age)
        self.studentId = student_id

    def get_id(self):
        return self.studentId  # returns the value of student id


idso = 42

if __name__ == "__main__":

    for name in Student.__dict__:
        print(name)
    # Create an object of the superClass
    person1 = Person("Richard", 23)
    # student2 = Student()
    # call member methods of the objects
    person1.show_age()
    # create an object of the subclass
    student1 = Student("Max", 23, "102")
    print(student1.get_id())
    student1.show_name()
