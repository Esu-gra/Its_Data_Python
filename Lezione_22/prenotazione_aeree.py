'''
Si vuole progettare un sistema in Python per
la gestione delle prenotazioni aeree. Il sistema
dovrà gestire diverse tipologie di voli, tra cui 
voli commerciali e voli charter.
'''

from abc import ABC, abstractmethod


class Volo(ABC):
    def __init__(self,codice:str,posti:int):
        self.codice=codice
        self.posti=posti
        self.prenotazioni=0
    
    @abstractmethod
    def prenota_posto(self):
        pass
    

    @abstractmethod
    def posti_disponibili(self):
        pass


class VoloCommerciale(Volo):
    def __init__(self, codice, posti):
        super().__init__(codice, posti)
        self.posti_economica=int(posti*0.7)
        self.posti_business=int(posti*0.2)
        self.posti_prima=posti-(self.posti_economica+self.posti_business)



        self.prenotazioni_economica=0
        self.prenotazione_business=0
        self.prenotazione_prima=0

    
    def posti_disponibili(self)->dict:
        disponibili_economica=self.posti_economica-self.prenotazioni_economica
        disponibili_business=self.posti_business-self.prenotazione_business
        disponibili_prima=self.posti_prima-self.prenotazione_prima
        posti_tot_disponibili=self.posti-self.prenotazioni

        return {
            'posti disponibili': max(0, posti_tot_disponibili),
            'classe economica': max(0, disponibili_economica),
            'classe business': max(0, disponibili_business),
            'prima classe': max(0, disponibili_prima)
        }
    

    def prenota_posto(self,posti,classe_servizio):
        msg=""
        

        

    



        
