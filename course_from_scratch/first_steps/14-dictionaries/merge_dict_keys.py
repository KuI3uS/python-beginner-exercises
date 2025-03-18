# 13.Napisz funkcję, która przyjmuje dwa słowniki i zwraca listę kluczy z obu słowników.

def lista_kluczy (slownik1, slownik2):
    return list(set(slownik1.keys()) | set(slownik2.keys()))

phone_number = {
    'Jakub' : 533490268,
    'Marta' : 503300400,
    'Daria' : 542255677
}

phone_number2 = {
    'Marta': 503300400,
    'Daria': 542255677,
    'Marcin': 500123789
}

wynik = lista_kluczy(phone_number, phone_number2)

print('lista telefonów: ',wynik)
