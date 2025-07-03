# === Classe astratta Volo ===
from abc import ABC, abstractmethod

class Volo(ABC):
    def __init__(self, codice: str, capacita_massima: int):
        self.codice = codice
        self.capacita_massima = capacita_massima
        self.prenotazioni = 0

    @abstractmethod
    def prenota_posto(self, *args, **kwargs):
        pass

    @abstractmethod
    def posti_disponibili(self):
        pass

# === Classe VoloCommerciale ===
class VoloCommerciale(Volo):
    def __init__(self, codice: str, capacita_massima: int):
        super().__init__(codice, capacita_massima)
        self.posti_economica = int(capacita_massima * 0.7)
        self.posti_business = int(capacita_massima * 0.2)
        self.posti_prima = capacita_massima - (self.posti_economica + self.posti_business)

        self.prenotazioni_economica = 0
        self.prenotazioni_business = 0
        self.prenotazioni_prima = 0

    def posti_disponibili(self):
        disponibili_economica = self.posti_economica - self.prenotazioni_economica
        disponibili_business = self.posti_business - self.prenotazioni_business
        disponibili_prima = self.posti_prima - self.prenotazioni_prima
        disponibili_totali = self.capacita_massima - self.prenotazioni
        return {
            'posti disponibili': max(0, disponibili_totali),
            'classe economica': max(0, disponibili_economica),
            'classe business': max(0, disponibili_business),
            'prima classe': max(0, disponibili_prima)
        }

    def prenota_posto(self, posti: int, classe_servizio: str):
        msg = ""
        classe_servizio = classe_servizio.lower()

        if self.prenotazioni >= self.capacita_massima:
            msg = f"Volo {self.codice} al completo!"
        elif classe_servizio not in ["economica", "business", "prima"]:
            msg = f"Classe '{classe_servizio}' non valida."
        else:
            disponibili = self.posti_disponibili()[f"classe {classe_servizio}"]
            if posti > disponibili:
                msg = f"Non è possibile riservare {posti} posti in classe {classe_servizio}. Numero posti disponibili: {disponibili}"
            else:
                if classe_servizio == "economica":
                    self.prenotazioni_economica += posti
                elif classe_servizio == "business":
                    self.prenotazioni_business += posti
                elif classe_servizio == "prima":
                    self.prenotazioni_prima += posti
                self.prenotazioni += posti
                msg = f"{posti} posti prenotati su {self.codice} in classe {classe_servizio}."

        print(msg)
        with open("report.txt", "a") as f:
            f.write(msg + "\n")
        return msg

# === Classe VoloCharter ===
class VoloCharter(Volo):
    def __init__(self, codice: str, capacita_massima: int, prezzo: float):
        super().__init__(codice, capacita_massima)
        self.prezzo = prezzo

    def prenota_posto(self):
        if self.prenotazioni == 0:
            self.prenotazioni = self.capacita_massima
            msg = f"Volo charter {self.codice} prenotato completamente per €{self.prezzo}."
        else:
            msg = f"Il volo charter {self.codice} è già prenotato."

        print(msg)
        with open("report.txt", "a") as f:
            f.write(msg + "\n")
        return msg

    def posti_disponibili(self):
        return self.capacita_massima - self.prenotazioni

# === Classe CompagniaAerea ===
class CompagniaAerea:
    def __init__(self, nome: str, prezzo_standard: float):
        self.nome = nome
        self.prezzo_standard = prezzo_standard
        self.flotta = []

    def aggiungi_volo(self, volo):
        self.flotta.append(volo)

    def rimuovi_volo(self, volo):
        if volo in self.flotta:
            self.flotta.remove(volo)

    def mostra_flotta(self):
        print(f"Ecco la flotta della compagnia aerea {self.nome}:")
        with open("report.txt", "a") as f:
            f.write(f"Ecco la flotta della compagnia aerea {self.nome}:\n")
            for volo in self.flotta:
                if isinstance(volo, VoloCommerciale):
                    msg = f"volo commerciale {volo.codice}"
                elif isinstance(volo, VoloCharter):
                    msg = f"volo charter {volo.codice}"
                print(msg)
                f.write(msg + "\n")

    def guadagno(self):
        totale = 0.0
        for volo in self.flotta:
            if isinstance(volo, VoloCommerciale):
                totale += (
                    volo.prenotazioni_economica * self.prezzo_standard +
                    volo.prenotazioni_business * self.prezzo_standard * 2 +
                    volo.prenotazioni_prima * self.prezzo_standard * 3
                )
            elif isinstance(volo, VoloCharter):
                if volo.prenotazioni == volo.capacita_massima:
                    totale += volo.prezzo
        msg = f"Dalla vendita dei biglietti aerei, la compagnia aerea {self.nome} ha guadagnato {round(totale, 2)} euro"
        print(msg)
        with open("report.txt", "a") as f:
            f.write(msg + "\n")
        return round(totale, 2)

# === Codice driver ===
open("report.txt", "w").close()  # Pulisce il file report.txt

# Volo commerciale COM123
com123 = VoloCommerciale("COM123", 100)
print("Posti disponibili sul volo commerciale COM123:")
print(com123.posti_disponibili())
com123.prenota_posto(70, "economica")
print(com123.posti_disponibili())
com123.prenota_posto(20, "business")
print(com123.posti_disponibili())
com123.prenota_posto(70, "prima")
print(com123.posti_disponibili())
com123.prenota_posto(10, "prima")
print(com123.posti_disponibili())
com123.prenota_posto(1, "economica")

# Volo charter CHA456
cha456 = VoloCharter("CHA456", 200, 20000.0)
print(f"Posti disponibili sul volo charter CHA456: {cha456.posti_disponibili()}")
cha456.prenota_posto()
cha456.prenota_posto()

# Secondo volo commerciale COM456
com456 = VoloCommerciale("COM456", 150)
com456.prenota_posto(100, "economica")

# Compagnia aerea ITA
ita = CompagniaAerea("ITA", 60.90)
ita.aggiungi_volo(com123)
ita.aggiungi_volo(com456)
ita.mostra_flotta()
ita.guadagno()
