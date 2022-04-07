class Student: #student class
  def__init__(self, rollNo, name) #define roll number and name when the object of studnt is created
self.rollNo = rollNo


self.name = name#initialize name
def display(self):#display method of student
 print(f'Student Roll No: {self.rollNo}')##print roll number of student
print(f'Student Name: {self.name}')#print name of student
class Exam(Student):#exam class
 def__init__(self, rollNo, name, subject)#define roll number, name and
super().__init__(rollNo, name)#initialize  roll number and name from student
self.subject = subject#initialize subjects
def display(self):#display method of exam
 super().display()#display roll number and name from student

for i in range(len(self.subject)):
    print(f'Subject {i+1} Marks: {self.subject[i]}')#print marks of subject
class Result(Exam):#class result
 total_marks = 0
def __init__(self, rollNo, name, subject):#define roll number, name , subject
 super().__init__(rollNo, name, subject)#initialize roll numer, name, subject from exam class
self.total_marks = sum(subject)#do sum of all marks
def display(self):#display method of result method
 super().display()#display roll number, name and subject
print(f'Total Marks: {self.total_marks}')
if __name__ == '__main__':student = Student(1,'Brijesh')
student.display()
print()
exam = Exam(2, 'Pratik', [18, 13, 8])
exam.display()
print()
result = Result(3, 'Smit', [10, 10, 15])
result.display()
print()
