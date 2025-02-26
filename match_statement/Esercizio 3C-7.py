

i_lancio=1
i_t=0
i_c=0
perc_t=0
perc_c=0

while True:
    if i_lancio<=8:
         lancio=input("lancio t/c: ")
         i_lancio+=1
         match lancio:
              case lancio if lancio=="t":
                   i_t+=1
              case lancio if lancio=="c":
                   i_c+=1
    

    else:
        
         break




perc_t=(i_t/8)*100
perc_c=(i_c/8)*100
print(f"totale testa: {i_t}")
print(f"percentuale testa: {perc_t:.2f}")

print(f"totale croce: {i_c}")
print(f"percentuale croce: {perc_c: .2f}")