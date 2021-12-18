#%%
#Tutaj będzie główny kod gry kółko i krzyżyk

plansza_do_gry = {
    "7" : " ", "8" : " ", "9" : " ",
    "4" : " ", "5" : " ", "6" : " ",
    "1" : " ", "2" : " ", "3" : " ",
}

klawisze_gry = []

for key in plansza_do_gry:
    klawisze_gry.append(key)

def drukuj_plansze(pole):
    print(f"{pole['7']}|{pole['8']}|{pole['9']}")
    print('-+-+-')
    print(f"{pole['4']}|{pole['5']}|{pole['6']}")
    print('-+-+-')
    print(f"{pole['1']}|{pole['2']}|{pole['3']}")


print(plansza_do_gry)
print(klawisze_gry)

drukuj_plansze(plansza_do_gry)


# %%
