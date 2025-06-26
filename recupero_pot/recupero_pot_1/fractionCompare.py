from frazioni import Frazione,semplificata


def fractionCompare(originali:list[Frazione],semplificati:list[Frazione]):
    for x,y in zip(originali,semplificati):
        val_orig=x.value()
        val_sempli=y.value()
        print(f"Valore frazione originale: {val_orig} --- Valore frazione ridotta: {val_sempli}")



if __name__ == "__main__":
    l = [Frazione(7, 13), Frazione(14, 26), Frazione(18, 24)]
    l_semplici = semplificata(l)
    fractionCompare(l, l_semplici)


