nome=input("Inserire nome: ")
vendita=int(input("inserire numero di vendite: "))

max_nome=nome
max_vendita=vendita



min_nome=nome
min_vendita=vendita
i=0

for y in range(4):
    if i==3:

        break
    else:
        new_nome=input("inserire nome: ")
        new_vendita=int(input("inserire nuova vendita: "))
        if new_vendita> max_vendita:
            max_nome=new_nome
            max_vendita=new_vendita
            i+=1
        else:
            if new_vendita<min_vendita:
                min_nome=new_nome
                min_vendita=new_vendita
                i+=1
            else:
                i+=1

    print(f"nome_max:{max_nome }, vendita massima: {max_vendita}")
    print(f"nome_min: {min_nome}, vendita min {min_vendita}")