'''

Completion requirements
Sistema di Prenotazione Cinema
Sviluppa un sistema in Python che gestisca le
prenotazioni per un cinema. Il cinema ha diverse
sale, ognuna con un diverso film in programmazione. 
Gli utenti possono vedere quali film sono disponibili e
prenotare posti per un determinato spettacolo.
'''

class Film:
    def __init__(self,titolo:str,durata:int):
        self.titolo=titolo
        self.durata=durata
    


class Sala:
    def __init__(self,id:str,film_atttuale:Film,film_in_programma:Film,posti_totali:int,posti_prenotati:int):
        self.id=id
        self.fa=film_atttuale
        self.fp=film_in_programma
        self.pt=posti_totali
        self.pp=posti_prenotati

    def prenota_posti(self,num_posti):
        if num_posti <= self.pt:
            self.pt=self.pt-num_posti
            print("posti pronotati")
        return self.pt
    def posti_disponibili(self):
        return f"Posti disponibili: {self.prenota_posti}"


class Cinema:
    def __init__(self):
        self.sale=[Sala]
    
    def aggiungi_sala(self,sala:Sala):
        self.sale.append(sala)
        print("Sala aggiunta con successo")
        return self.sale
    
    def prenota_film(self,titolo_film:str,num_post:int):
        if titolo_film==self.sale
                    

        

        