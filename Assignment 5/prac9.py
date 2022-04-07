"""
ID : 20CE015
NAME : Ayush Dabhi
GITHUB REPOSITORY LINK :
"""


class Student:
    def __init__(self, roll_number, name):
        self.rollNumber = roll_number
        self.name = name


class Exam(Student):
    sub1 = 0
    sub2 = 0
    sub3 = 0
    sub4 = 0
    sub5 = 0
    sub6 = 0

    def __init__(self, roll_number, name, sub1, sub2, sub3, sub4, sub5, sub6):
        super().__init__(roll_number, name)
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.sub4 = sub4
        self.sub5 = sub5
        self.sub6 = sub6

    def marks(self):
        print("Marks in each subject...\nSubject 1 : ", self.sub1)
        print("Subject 2 : ", self.sub2)
        print("Subject 3 : ", self.sub3)
        print("Subject 4 : ", self.sub4)
        print("Subject 5 : ", self.sub5)
        print("Subject 6 : ", self.sub6)


class Result(Exam):
    def __init__(self, roll_number, name, sub1, sub2, sub3, sub4, sub5, sub6):
        super().__init__(roll_number, name, sub1, sub2, sub3, sub4, sub5, sub6)

    total_marks = Exam.sub1 + Exam.sub2 + Exam.sub3 + Exam.sub4 + Exam.sub5 + Exam.sub6
    print(Exam.sub1)
    percent = total_marks / 6

    def total(self):
        print("Total Marks : ", self.total_marks)

    def percentage(self):
        print("Percentage : ", self.percent)


r1 = Result(1, 'Bhargav', 26, 28, 21, 27, 25, 20)
r1.total()
r1.percentage()
