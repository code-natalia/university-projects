# Gonkiewicz Natalia, Mariola Michalska 22.06.2023

import sys

słownik_wyrazów = {}

def funkcja(nazwa_pliku):
    f = open(nazwa_pliku, 'r')

    lista_wyrazów_pliku = []      

    for wiersz in f:

        wiersz = wiersz.strip()

        if wiersz in słownik_wyrazów and wiersz not in lista_wyrazów_pliku:
            słownik_wyrazów[wiersz] += 1 
            lista_wyrazów_pliku.append(wiersz)
        
        elif wiersz not in słownik_wyrazów: 
            słownik_wyrazów[wiersz] = 1
            lista_wyrazów_pliku.append(wiersz)

    f.close()

liczba_plików = len(sys.argv) 

for i in range(1,liczba_plików):  
    funkcja(sys.argv[i])         


s = open('wynik', 'w')

for klucz in słownik_wyrazów:
    s.write(klucz + " " + str(słownik_wyrazów[klucz]) + "\n")

s.close()
