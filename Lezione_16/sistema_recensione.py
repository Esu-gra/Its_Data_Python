class Media:
    _title: str
    _reviews: list[int]

    def __init__(self, title: str):
        self.set_title(title)
        self._reviews = []

    def set_title(self, title: str):
        self._title = title

    def get_title(self):
        return self._title

    def aggiungiValutazione(self, voto: int):
        if not 1 <= voto <= 5:
            raise ValueError("Il voto deve essere un numero intero compreso tra 1 e 5")
        self._reviews.append(voto)

    def getMedia(self):
        if len(self._reviews) == 0:
            raise ValueError("Nessuna recensione disponibile.")
        media = sum(self._reviews) / len(self._reviews)
        return round(media, 2)

    def getRate(self):
        media_arro = round(self.getMedia())
        match media_arro:
            case 1:
                return "Terribile"
            case 2:
                return "Brutto"
            case 3:
                return "Normale"
            case 4:
                return "Bello"
            case 5:
                return "Grandioso"

    def ratePercentuale(self, voto):
        tot = len(self._reviews)
        if tot == 0:
            return 0.0
        count = self._reviews.count(voto)
        percentuale = (count / tot) * 100
        return round(percentuale, 2)

    def recensione(self):
        if len(self._reviews) == 0:
            print(f"TITOLO: {self.get_title()}")
            print("Nessuna recensione disponibile.")
            return

        media = self.getMedia()
        giudizio = self.getRate()

        etichette = {
            1: "Terribile",
            2: "Brutto",
            3: "Normale",
            4: "Bello",
            5: "Grandioso"
        }

        print(f"Titolo del Film: {self.get_title()}")
        print(f"Voto Medio: {media:.2f}")
        print(f"Giudizio: {giudizio}")
        for voto in range(1, 6):
            print(f"{etichette[voto]}: {self.ratePercentuale(voto):.2f}%")


class Film(Media):
    pass
film2=Film("Inseption")
if __name__ == "__main__":
    
    voti = [5, 4, 5, 3, 5, 2, 1, 4, 5, 3]
    for voto in voti:
        film2.aggiungiValutazione(voto)
    film2.recensione()
