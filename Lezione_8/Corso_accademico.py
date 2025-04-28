# Copia qui di seguito il codice di Realizzazione e Gestione Corsi ITS - Parte 1 
class Room:
    def __init__(self, id, floor, seats):
        self._id = id
        self.floor = floor
        self.seats = seats

    def get_id(self):
        return self._id

    def get_floor(self):
        return self.floor

    def get_seats(self):
        return self.seats

    def get_area(self):
        return self.seats * 2


class Building:
    def __init__(self, name, address, floors):
        self.name = name
        self.address = address
        self.floors = floors  
        self.rooms = []

    def get_floors(self):
        return self.floors

    def get_rooms(self):
        return self.rooms

    def add_room(self, room: Room):
        if self.floors[0] <= room.get_floor() <= self.floors[1]:
            if room.get_id() not in [r.get_id() for r in self.rooms]:
                self.rooms.append(room)

    def area(self):
        return sum(room.get_area() for room in self.rooms)


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



class Course:
    def __init__(self, name):
        self.name = name
        self.groups = []  # Lista di gruppi che fanno parte del corso

    def register(self, student):
        # Registra lo studente nel primo gruppo disponibile che non ha ancora raggiunto il limite
        for group in self.groups:
            if len(group.get_students()) < group.limit:
                group.get_students().append(student)
                student.set_group(group)  # Imposta il gruppo dello studente
                return True  # Studente registrato con successo
        return False  # Non ci sono gruppi disponibili per lo studente

    def get_groups(self):
        return self.groups

    def add_group(self, group):
        self.groups.append(group)