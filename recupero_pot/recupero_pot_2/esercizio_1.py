
import math
def calcolo_costo_parch(h):
    if h<=3:
        costo=2.00
    else:
        extra=math.ceil(h-3)
        costo=2.00+(extra*0.50)
    return min(round(costo,2),10.0)


clients = [
    {"car": 1, "hours": 1.5},
    {"car": 2, "hours": 4.0},
    {"car": 3, "hours": 24.0}
]


print(f"{'Car':<10}{'Hours':<10}{'Charge':<10}")
tot_ore=0
tot_costo=0


for client in clients:
   car=clients["car"]
   hours=clients["hours"]
   charge=calcolo_costo_parch(hours)
   tot_hours+=hours
   tot_charge+=charge
   print({""})
