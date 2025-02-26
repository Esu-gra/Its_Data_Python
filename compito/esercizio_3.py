string=input("inserire parola: ")
string_inv=" "


for x in string:
    string_inv=x+string_inv
print(f"parola invertita: {string_inv}")