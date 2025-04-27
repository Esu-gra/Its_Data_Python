class Person:
    def __init__(self,cf:str , name:str,surname:str,age:int):
        self.name=name
        self.surname=surname
        self.cf=cf
        self.age=age

    def set_group(self,group):
        self.group=group




class Student(Person):
    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)
        self.group = None 

    def set_group(self, group):
        self.group = group




class Lecturer(Person):
    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)











class Group:
    def __init__(self, name, limit, students=None, lecturers=None):
        self.name = name
        self.limit = limit
        self.students = students if students is not None else []
        self.lecturers = lecturers if lecturers is not None else []

    def get_name(self):
        return self.name

    def get_limit(self):
        return f"Limite Studenti: {self.limit}"

    def get_students(self):
        return self.students

    def get_limit_lecturers(self):
        return max(1, len(self.students) // 10)

    def add_student(self, student):
        if len(self.students) < self.limit:
            self.students.append(student)
            return True
        return False

    def add_lecturer(self, lecturer):
        if len(self.lecturers) < self.get_limit_lecturers():
            self.lecturers.append(lecturer)
            return True
        return False