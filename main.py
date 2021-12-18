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

def gra():
    gracz = 'X'
    licznik = 0
    for i in range(10):
        drukuj_plansze(plansza_do_gry)
        move = input(f'To jest ruch, {gracz}. Wybierz miejsce postawienia znaku!')
        if plansza_do_gry[move] == " ":
            plansza_do_gry[move] = gracz
            licznik += 1
        else:
            print("Pole jest już zajęte!\nWstaw swój znak w inne miejsce.")    
            continue
        if licznik >= 5:
            if plansza_do_gry['7'] == plansza_do_gry['8'] == plansza_do_gry['9'] != ' ':
                drukuj_plansze(plansza_do_gry)
                print('\nKoniec Gry\n')
                print(f"Wygrał Gracz: {gracz}!")
                break
            elif plansza_do_gry['4'] == plansza_do_gry['5'] == plansza_do_gry['6'] != ' ':
                drukuj_plansze(plansza_do_gry)
                print('\nKoniec Gry\n')
                print(f"Wygrał Gracz: {gracz}!")
                break
            elif plansza_do_gry['1'] == plansza_do_gry['2'] == plansza_do_gry['3'] != ' ':
                drukuj_plansze(plansza_do_gry)
                print('\nKoniec Gry\n')
                print(f"Wygrał Gracz: {gracz}!")
                break
            #koniec wygranych poziomych
            elif plansza_do_gry['7'] == plansza_do_gry['4'] == plansza_do_gry['1'] != ' ':
                drukuj_plansze(plansza_do_gry)
                print('\nKoniec Gry\n')
                print(f"Wygrał Gracz: {gracz}!")
                break
            elif plansza_do_gry['8'] == plansza_do_gry['5'] == plansza_do_gry['2'] != ' ':
                drukuj_plansze(plansza_do_gry)
                print('\nKoniec Gry\n')
                print(f"Wygrał Gracz: {gracz}!")
                break
            elif plansza_do_gry['9'] == plansza_do_gry['6'] == plansza_do_gry['3'] != ' ':
                drukuj_plansze(plansza_do_gry)
                print('\nKoniec Gry\n')
                print(f"Wygrał Gracz: {gracz}!")
                break
            #koniec wygranych pionowych
            elif plansza_do_gry['7'] == plansza_do_gry['5'] == plansza_do_gry['3'] != ' ':
                drukuj_plansze(plansza_do_gry)
                print('\nKoniec Gry\n')
                print(f"Wygrał Gracz: {gracz}!")
                break
            elif plansza_do_gry['1'] == plansza_do_gry['5'] == plansza_do_gry['8'] != ' ':
                drukuj_plansze(plansza_do_gry)
                print('\nKoniec Gry\n')
                print(f"Wygrał Gracz: {gracz}!")
                break

# %%
