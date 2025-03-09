# 10.Napisz funkcję, która przyjmuje liczbę i zwraca odpowiednią wiadomość w zależności od tego, czy liczba jest dodatnia, ujemna, czy zerowa.

def positive_negative_zero(num):
    if num < 0:
        return 'negative'
    elif num > 0:
        return 'positive'
    else:
        return 'zero'


print(positive_negative_zero(10))