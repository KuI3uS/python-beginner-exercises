# 17.Napisz funkcję, która przyjmuje listę liczb od użytkownika, a następnie zwraca te liczby, które występują na liście więcej niż raz.

def repeated_numbers(lista):
    licznik = {}

    for i in lista:
        if i in licznik:
            licznik[i] += 1
        else:
            licznik[i] = 1
    duplikat = [liczba for liczba, ilosc in licznik.items() if  ilosc > 1]

    return duplikat

wejscie = input('your numbers : ')
lista_liczb = list(map(int, wejscie.split()))

wynik = repeated_numbers(lista_liczb)
print('your numbers : ', wynik)
