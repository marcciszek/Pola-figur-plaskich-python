import time
import os
import math

print('Wybierz figure\n 1.Kwadrat\n 2.Prostokat\n 3.Trojkat\n 4.Kolo: ') #\n przechodzi do nowej linii
print("Podaj odpowiadajaca cyfre: ")
while True: #petla sprawdzajaca poprawnosc podanego wyboru
    figura = input()
    if figura == '1' or '2' or '3' or '4': #dostepne wybory
        break
    else:
        os.system('cls')
        print('Wybierz figure\n 1.Kwadrat\n 2.Prostokat\n 3.Trojkat\n 4.Kolo: ')
        print('Podaj poprawna cyfre')

os.system('cls') #czyszczenie konsoli

if figura == '1': #figura jest stringiem, dlatego wybory cyfry sa postaci 'x'
    print("Wybrales kwadrat\nPodaj dlugosc boku")
    dl_bok = float(input()) #dlugosc boku pobierana jako liczba zmiennoprzecinkowa
    pole = dl_bok**2
    os.system('cls')
    print('Pole powierzchni dla kwadratu wynosi')
    print(dl_bok,'^ 2 =',pole)
    
if figura == '2':
    print("Wybrales prostokat\nPodaj dlugosc boku a")
    dl_bok_a = float(input())
    print("Podaj dlugosc boku b")
    dl_bok_b = float(input())
    pole = dl_bok_a*dl_bok_b
    os.system('cls')
    print('Pole powierzchni dla prostokatu wynosi')
    print(dl_bok_a,' * ',dl_bok_b,' = ',pole)

if figura == '3':
    print("Wybrales trojkat\nPodaj dlugosc podstawy")
    dl_podstawy = float(input())
    print("Podaj wysokosc")
    wysokosc = float(input())
    pole = (dl_podstawy * wysokosc) / 2.0
    os.system('cls')
    print('Pole powierzchni dla trojkata wynosi')
    print('(',dl_podstawy,' * ',wysokosc,')','/ 2 = ',pole)


if figura == '4':
    print("Wybrales kolo\nPodaj dlugosc promienia")
    promien = float(input())
    pole = promien**2*math.pi
    print('pole powierzchni dla kola wynosi')
    print(promien,'^ 2 * PI = ',pole)

time.sleep(10)

