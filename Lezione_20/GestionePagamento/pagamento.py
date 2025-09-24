class Pagamento:
    _importo: float

    def __init__(self):
        self._importo = None

    def set_importo(self, i: float):
        self._importo = i

    def get_importo(self):
        return round(self._importo, 2)


class PagamentoContanti(Pagamento):  # corretto nome della classe
    def __init__(self):
        super().__init__()

    def dettaglioPagamento(self):
        return f"Pagamento in contanti: €{self.get_importo():.2f}"

    def inPezziDa(self):
        resto = int(round(self.get_importo() * 100))  # <-- intero in centesimi

        valori = [50000, 20000, 10000, 5000, 2000, 1000, 500,
                  200, 100, 50, 20, 10, 5, 1]
        nomi = ["500€", "200€", "100€", "50€", "20€", "10€", "5€",
                "2€", "1€", "0,50€", "0,20€", "0,10€", "0,05€", "0,01€"]

        print("Scomposizione in pezzi:")
        l_v=len(valori)
        for i in range(l_v):
            v = valori[i]
            nome = nomi[i]

            quantita = resto // v
            if quantita > 0:
                if v >= 500:  # da 5€ in su → banconote
                    print(f"{int(quantita)} banconota/e da {nome}")
                else:         # sotto 5€ → monete
                    print(f"{int(quantita)} moneta/e da {nome}")
                    resto = resto % v
        return resto

        


p=PagamentoContanti()
p.set_importo(1200)
print(p.inPezziDa())