import time     #biblioteka dzięki ktorej zatrzymujemy program na okreslony czs
import os       #biblioteka pozwalajaca czyscic okno konsoli
import math     #biblioteka zawierajaca liczbe PI

dostepne_wybory = ('1','2','3','4') #pula wyborow dostepnych dla uzytkownika
glowne_menu='''
 Wybierz figure
 1.Kwadrat
 2.Prostokat
 3.Trojkat
 4.Kolo:
'''

print(glowne_menu)    #\n przechodzi do nowej linii
print(" Podaj odpowiadajaca cyfre")

while True:     #petla sprawdzajaca poprawnosc podanego wyboru
    wybor_uzytkownika = input(' >')  #pobranie wyboru od uzytkownika
    if wybor_uzytkownika in(dostepne_wybory):  #sprawdzenie czy wybor jest dostepny
        break
    else:
        os.system('cls')
        print(glowne_menu)
        print(' Podaj poprawna cyfre')

os.system('cls') #czyszczenie konsoli

if wybor_uzytkownika == '1':    #figura jest stringiem, dlatego wybory sa postaci 'x'
    print("\n Wybrales kwadrat\n\n Podaj dlugosc boku")
    dl_bok = float(input(' >'))  #dlugosc boku pobierana jako liczba zmiennoprzecinkowa
    pole = dl_bok**2
    os.system('cls')
    print(f"\n Pole kwadratu {dl_bok} ^ 2 = {pole}")
    
if wybor_uzytkownika == '2':
    print("\n Wybrales prostokat\n\n Podaj dlugosc boku a")
    dl_bok_a = float(input(' >'))
    print(" Podaj dlugosc boku b")
    dl_bok_b = float(input(' >'))
    pole = dl_bok_a*dl_bok_b
    os.system('cls')
    print(f"\n Pole prostokatu {dl_bok_a} * {dl_bok_b} = {pole}")

if wybor_uzytkownika == '3':
    print("\n Wybrales trojkat\n\n Podaj dlugosc podstawy")
    dl_podstawy = float(input(' >'))
    print(" Podaj wysokosc")
    wysokosc = float(input(' >'))
    pole = (dl_podstawy * wysokosc) / 2.0
    os.system('cls')
    print(f"\n Pole trojkata ({dl_podstawy} * {wysokosc}) / 2 = {pole}")


if wybor_uzytkownika == '4':
    print("\n Wybrales kolo\n\n Podaj dlugosc promienia")
    promien = float(input(' >'))
    pole = promien**2*math.pi
    os.system('cls')
    print(f"\n Pole kola {promien} ^ 2 * {round(math.pi,4)} = {round(pole,4)}")  #zaokraglenie(zmienna,ilosc miejsc po przecinku) 
    print()

time.sleep(10)
