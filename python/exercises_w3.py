# 1. Write a Python program to import a built-in array module and display the namespace of the said module.

# import array
#
# for name in array.__dict__:
#     print(name)
#
#
# # 2. Write a Python program to create a class and display the namespace of that class.
# class BaseClass:
#     def __init__(self):
#         for name in BaseClass.__dict__:
#             print(f'Name of namespace is {name}')

class Student(object):

    enrolled = True

    def __init__(self, name, age, grade, full_time):
        self.name = name
        self.age = age
        self.grade = grade
        self.full_time = full_time

    def print_details(self):
        print(self.__dict__)

class


if __name__ == "__main__":
    # BaseClass()
    s = Student('Aaron', 100, 11, True)
    print(Student.__dict__)
    s.print_details()
