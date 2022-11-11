class Student:
    def __init__ (self,regno,name,age):
         self.regno=regno
         self.name=name 
         self.age=age
    def Study(self):
            return "Iam studying"
    def Play(self):
            return "Iam playing"
    def Discuss(self):
            return "Iam discussing"  
    def __str__(self):
           return f"my name is{self.name}"
student_1=Student("s21b13/090","claire",32)
   
print(student_1) 
print(student_1.Study())  
print(student_1.Play())
print(student_1.Discuss())  
class Networkadmin(Student):
    def __init__(self):
        super().__init__(self,regno,name,age)
        return "i have been created"
student_2=Networkadmin("s21b13/070","claire",23)                   