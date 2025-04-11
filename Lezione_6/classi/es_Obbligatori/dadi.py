import random

class Dado:
    def __init__(self,lati=6):
        self.lati=lati

    def roll_die(self):
            print(random.randint(1,self.lati))




d1=Dado(6)
d2=Dado(10)
d3=Dado(20)

d1.roll_die()
d1.roll_die()
d1.roll_die()
d1.roll_die()
d1.roll_die()
d1.roll_die()
