class ContactManager:
    def __init__(self):
        self.contatti:dict={}
    

    def create_contact(self,name:str,phone_numbers:list[str]):
        if name in self.contatti:
            return "Errore:il contatto esiste già"
        self.contatti[name]=phone_numbers
        return {name:self.contatti[name]}
        

        
    def add_phone_number(self,contact_name:str,phone_number:str):
        if contact_name not in self.contatti:
            return "Errore: il contatto non esiste"
        if phone_number in self.contatti[contact_name]:
            return "Errore: il numero esiste gia"
        self.contatti[contact_name].append(phone_number)
        return {contact_name:self.contatti[contact_name]}
    
    def remove_phone_number(self, contact_name: str, phone_number: str):
        if contact_name not in self.contatti:
            return "Errore: il contatto non esiste"
        self.contatti[contact_name].remove(phone_number)
        return {contact_name:self.contatti[contact_name]}
    
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str):
        if contact_name not in self.contatti:
            return "Errore: il contatto non esiste"
        if old_phone_number not in self.contatti[contact_name]:
            return "Errore: il numero di telefono non è presente"
        
        index=self.contatti[contact_name].index(old_phone_number)
        self.contatti[contact_name][index]=new_phone_number
        return {contact_name:self.contatti[contact_name]}
    
    def list_contacts(self):
        return list(self.contatti.keys())
    
    def list_phone_numbers(self, contact_name: str):
        if contact_name not in self.contatti:
            return "Errore: il contatto non esiste"
        return self.contatti[contact_name]
    

    def search_contact_by_phone_number(self, phone_number: str):
        contatto=[name for name,num in self.contatti.items() if phone_number  in num]
        if contatto==False:
            return "Nessun contatto trovato"
        return contatto

cm = ContactManager()

print(cm.create_contact("Alice", ["123456789"]))
print(cm.add_phone_number("Alice", "987654321"))
print(cm.remove_phone_number("Alice", "123456789"))
print(cm.update_phone_number("Alice", "987654321", "111222333"))
print(cm.list_contacts())
print(cm.list_phone_numbers("Alice"))
print(cm.search_contact_by_phone_number("111222333"))