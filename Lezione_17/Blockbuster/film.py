class Film:
    _identificativo:int
    _titolo:str

    def __init__(self,id:int,titolo:str):
        self.setID(id)
        self._titolo=titolo

    def setID(self,i:int):
        self._identificativo=i
    
    def setTitle(self,t:str):
        self._titolo=t
    
    def getID(self):
        return self._identificativo
    
    def getTitle(self):
        return self._titolo
    
    def isEqual(self,otherFilm):
        if self.getID()==otherFilm:
            return True
    
    

        