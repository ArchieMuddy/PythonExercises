

class Student:

    school = 'SHS'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return ((self.m1 + self.m2 + self.m3)/3)

    @classmethod
    def info(cls):
        return cls.school

s1 = Student (34, 47, 32)
s2 = Student (89, 32, 12)

print(s1.average())
print(Student.info())

a = 5
b = 6

int.__add__(a,b)