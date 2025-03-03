città={"Roma":{"Paese":"Italia",
               "Popolazione":123000,
               "Curiosità":"Hanno rubato il colosseo"},

       "Barcellona":{"Paese":"Spagnia",
                     "Popolazione":234000,
                     "Curiosità":"Gaudi ha deciso di ricostruire la S.Familia"},

       "Bruge":{"Paese":"Paesi Bassi",
                "Popolazione":23000,
                "Curiosità":"Hanno rubato il colosseo"}}

for k,v in città.items():
    print(f"{k}")
    for i , z in v.items():
        print(f"{i}: {z}")
    # print(f"{k}:{', ' .join(map(str,z))
    # }")