


#persone-studenti e docenti-in gruppo di studio
#corsi



# parte uno
#auele ed edifici

#classe Room -> aula (ID(id),un piano(floor),numero posti (seats),un area(area->il doppio dei posti))
               #metodi ---> get_id()-> restituisce l'ID dell'aula , get_floor()--> restituisce il piano dell'aula , 
               #get_seats()--> restituisce il numero dei posti dell'aula , get_area--> restituisce l'area dell'aula 


#classe Building -> Edificio (nome(nome),un indirizzo(andress),un intervallo di piani(floors),una lista di aule(rooms))
               #metodi ---> get_floors()-> restituisce l'intervallo di piani dell'edificio , get_rooms()--> restituisce la lista della aule della lista , 
              #get_room()--> aggiunge aule nell'edificio , solo se il piano dell'aula è compreso nell'intervallo di piani dell'edificio, area()--> restituisce l'area dell'edificio sommandi le areee di tutte le aule 

class Room:
    def __init__(self,id,floor,seats,area):
        self._id=id
        self.floor=floor
        self.seats=seats
        self.area=area

    def get_id(self):
        return self._id
    def get_floor(self):
        return self.floor
    def get_seats(self):
        return self.seats
    def get_area(self):
        return self.seats*2


class Building(Room):
    def __init__(self,name,andress,floors,rooms:list):
        self.name=name
        self.andress=andress
        self.floors=floors
        self.rooms=[]

    def get_floors(self):
        return self.floors
    
    def get_rooms(self):
        return self.rooms
    
    def add_room(self,room:Room):
        if self.floor[0] <= room.get_floor()<=self.floors[1]:
            if room.get_id() not in [r.get_id() for r in self.rooms]:
             self.rooms.append(room)
        else:
            return "Non appartiene a questo piano"
        
    def area(self):
        return sum(room.get_area() for room in self.rooms)


