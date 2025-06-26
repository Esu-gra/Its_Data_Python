class Documento:

    def __init__(self, testo: str):
        self.setText(testo)

    def setText(self, testo: str):
        self._testo = testo

    def getText(self) -> str:
        return self._testo
    

    def isInText(self, parola_chiave: str) -> bool:
        return parola_chiave in self._testo.split()
    













class Email(Documento):
    def __init__(self, mittente="", destinatario="", titolo="", testo=""):
        super().__init__(testo)
        self.mittente = mittente
        self.destinatario = destinatario
        self.titolo = titolo

    def getMittente(self):
        return self.mittente

    def setMittente(self, mittente):
        self.mittente = mittente

    def getDestinatario(self):
        return self.destinatario

    def setDestinatario(self, destinatario):
        self.destinatario = destinatario

    def getTitolo(self):
        return self.titolo

    def setTitolo(self, titolo):
        self.titolo = titolo

    def getText(self):
        return (
            f"Da: {self.mittente}, A: {self.destinatario}\n"
            f"Titolo: {self.titolo}\n"
            f"Messaggio: {self.getText()}"
        )
    
    def writeToFile(self, percorso):
        try:
            with open(percorso, 'w') as file:
                file.write(self.getText())
            print(f"Contenuto scritto con successo in: {percorso}")
        except Exception as e:
            print(f"Errore durante la scrittura su file: {e}")



    
    


    

    

    

    

    
        





        
doc = Documento("Questo è un documento di esempio")
print(doc.getText())               # Output: Questo è un documento di esempio
print(doc.isInText("documento"))   # Output: True
print(doc.isInText("mancante"))    # Output: False



email = Email()
email.setMittente("alice@example.com")
email.setDestinatario("bob@example.com")
email.setTitolo("Incontro")
email.setText("Ciao Bob, possiamo incontrarci domani?")

email.writeToFile("email_output.txt")
