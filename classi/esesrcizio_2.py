class Student:
    def __init__(self,name:str,studyProgram:str,age:int,gender:str):
        personCounr=0
        self.name=name
        self.studyProgram=studyProgram
        self.age=age
        self.gender=gender



    def printInfo(self):
        print(f"Name: {self.name}\nStudy Program: {self.studyProgram}\nAge:{self.age}\nGender:{self.gender}")





stu1=Student("Aldo","Economia",23,"M")

stu2=Student("Marius","Data",23,"M")
stu3=Student("Lola","Giurisp",33,"F")
stu1.printInfo()
print("-------------------------------")
stu2.printInfo()
print("-------------------------------")
stu3.printInfo()