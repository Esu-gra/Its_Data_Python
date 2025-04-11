numero_fortunato={'Pappa':[12,3,4,5],
                  'Tony':[22,34,5],
                  'Peppe':[23,5,6,89],
                  'Lollo':[23,78,8]}


for k,v in numero_fortunato.items():
    print(f"{k}:{', ' .join(map(str,v))}")

