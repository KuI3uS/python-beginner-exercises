#Podaj liczbe początkową
liczba = int(input("Podaj liczbe początkową :"))
liczba1 = int(input("Podaj liczbe koncową :"))

#	1.	Poprosi użytkownika o podanie dwóch liczb – jednej będącej początkiem przedziału, a drugiej końcem.
#   2.	Wyświetli wszystkie liczby w tym przedziale, ale tylko te, które są podzielne przez 3.

for i in range(liczba,liczba1):
    if i % 3 == 0:
        print(i)
